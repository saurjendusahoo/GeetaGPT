import streamlit as st
import os
from dotenv import load_dotenv
from rag_engine import AGEngine

# Load environment variables
load_dotenv()

st.set_page_config(page_title="GeetaGPT", page_icon="🏹")

st.title("GeetaGPT")

st.markdown("""
> *“Yield not to this impotence, O Partha! It does not befit thee. Cast off this petty faint-heartedness and arise, O Chastiser of Enemies!”*
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your question, if you dare..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("The Charioteer contemplates the scriptures..."):
            try:
                engine = AGEngine()
                chain = engine.get_chain()
                if chain:
                    response = chain.invoke(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    msg = "I cannot find my voice (Index not found). Please ensure the data is set up."
                    st.markdown(msg)
                    st.session_state.messages.append({"role": "assistant", "content": msg})
            except Exception as e:
                st.error(f"An error occurred: {e}")

