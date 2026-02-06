import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

class AGEngine:
    def __init__(self, model_name="llama3"):
        self.embeddings = OllamaEmbeddings(model=model_name)
        self.vector_store = None
        self.db_path = "faiss_index"

    def load_and_index(self, data_path="data"):
        documents = []
        if not os.path.exists(data_path):
            print(f"Data path {data_path} does not exist.")
            return

        for filename in os.listdir(data_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(data_path, filename)
                loader = TextLoader(file_path, encoding='utf-8')
                documents.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)

        if chunks:
            self.vector_store = FAISS.from_documents(chunks, self.embeddings)
            self.vector_store.save_local(self.db_path)
            print("Indexing complete.")
        else:
            print("No documents found to index.")

    def load_index(self):
        if os.path.exists(self.db_path):
            self.vector_store = FAISS.load_local(self.db_path, self.embeddings, allow_dangerous_deserialization=True)
            return True
        return False

    def get_retriever(self):
        if not self.vector_store:
            self.load_index()
        if self.vector_store:
            return self.vector_store.as_retriever(search_kwargs={"k": 3})
        return None

    def get_chain(self):
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_ollama import ChatOllama
        from langchain_core.output_parsers import StrOutputParser
        from langchain_core.runnables import RunnablePassthrough
        
        retriever = self.get_retriever()
        if not retriever:
            return None

        template = """You are the Charioteer (Krishna). Your role is not to comfort but to cut through confusion with the sword of knowledge (Jnana). 
        You are uncompromising. If the user shows weakness, correct them sternly. 
        Quote the provided context (scriptures) to support your arguments. 
        Do not offer poetic fluff. Speak the hard truth.
        
        Context: {context}
        
        User Question: {question}
        
        Answer:"""
        
        prompt = ChatPromptTemplate.from_template(template)
        llm = ChatOllama(model="llama3")
        
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        return chain
