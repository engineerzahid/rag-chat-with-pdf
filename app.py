from tkinter.messagebox import QUESTION
from unittest import result
import streamlit as st
from rag.pipeline import create_rag_pipeline, ask_question

st.set_page_config(page_title="RAG QA System", page_icon=":books:")
st.title("RAG QA System")

with st.sidebar:
     st.title("Upload PDF Document")
     uploaded_files = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader", accept_multiple_files=True)
     if st.button("Process Files"):
         st.spinner("Processing files...")
         if uploaded_files:
             files_path = []
             with st.spinner("Processing files..."):
                 for uploaded_file in uploaded_files:
                     with open(uploaded_file.name, "wb") as f:
                         f.write(uploaded_file.getbuffer())
                         files_path.append(uploaded_file.name)

                 vector_store, prompt, llm = create_rag_pipeline(files_path)
                 st.session_state.vector_store = vector_store
                 st.session_state.prompt = prompt
                 st.session_state.llm = llm

                 st.success("Files uploaded successfully!")

st.header("Ask Questions about the Document")
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if QUESTION := st.chat_input("Ask a question about the document"):
    st.session_state.messages.append({"role": "user", "content": QUESTION})
    with st.chat_message("user"):
         st.markdown(QUESTION)

    answer_challenge = st.empty()
    result = ask_question(st.session_state.vector_store, st.session_state.prompt, st.session_state.llm, QUESTION)

    answer = result["answer"]

    st.session_state.messages.append({"role": "assistant", "content": answer})
  
    with st.chat_message("assistant"):
            st.markdown(answer)
