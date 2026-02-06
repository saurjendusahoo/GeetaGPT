# GeetaGPT 🏹

> *"Yield not to this impotence, O Partha! It does not befit thee. Cast off this petty faint-heartedness and arise, O Chastiser of Enemies!"*

**GeetaGPT** is an AI agent designed to act as **Krishna**, capable of answering spiritual questions using the **Bhagavad Gita** and other Hindu scriptures.

Unlike typical comforting AI assistants, this agent adopts the persona of the Charioteer—providing direct, uncompromising, and knowledge-based answers. It challenges deviations from Dharma and logic, delivering the "raw, hard truths" of the scriptures.

## 🚀 Features

- **Persona-based AI**: Speaks with the authority and tone of Krishna.
- **RAG Engine**: Uses Retrieval-Augmented Generation to ground answers in provided text files (scriptures).
- **Local Privacy**: Runs locally using **Ollama** and **Streamlit**.
- **Vector Search**: Utilizes **FAISS** for efficient retrieval of relevant scriptural context.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.8+**
2.  **[Ollama](https://ollama.com/)**: Required for running the LLM locally.

### Setup Ollama

Pull the `llama3` model (default used by the engine):

```bash
ollama pull llama3
```

## 📦 Installation

1.  **Clone the repository** (or download the source code).
2.  **Install Python dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration & Data Setup

1.  **Prepare your data**:
    - Place your text files (e.g., `gita.txt`, `upanishads.txt`) inside the `data/` directory.
    - The agent will use these files as its source of truth.

2.  **Index the data**:
    - Run the setup script to create the vector database.
    
    ```bash
    python setup_data.py
    ```
    
    *This will generate a `faiss_index` directory containing the indexed data.*

3.  **Check available models** (Optional):
    - Verify that `llama3` is available.
    
    ```bash
    python check_models.py
    ```

## ▶️ How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

Open your browser at the URL provided (usually `http://localhost:8501`) to converse with the Charioteer.

## 📂 Project Structure

- `app.py`: Main Streamlit application file.
- `rag_engine.py`: Core logic for RAG, embedding, and LLM interaction.
- `setup_data.py`: Script to process text files in `data/` and build the FAISS index.
- `check_models.py`: Helper script to list available Ollama models.
- `data/`: Directory for your source text files.
- `faiss_index/`: storage for the vector embeddings.

