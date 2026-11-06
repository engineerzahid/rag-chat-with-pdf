import streamlit as st
from rag.pipeline import create_rag_pipeline, ask_question

st.set_page_config(page_title="RAG Chatbot", page_icon=":robot_face:", layout="wide")
st.title("RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


if "rag_ready" not in st.session_state:
    st.session_state.rag_ready = False


with st.sidebar:
    st.header("Upload PDF Files")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)
    if uploaded_files:
        files_path = []
        for uploaded_file in uploaded_files:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            files_path.append(uploaded_file.name)
        vector_store, prompt, llm = create_rag_pipeline(files_path)
        st.session_state.vector_store = vector_store
        st.session_state.prompt = prompt
        st.session_state.llm = llm
        st.session_state.rag_ready = True
        st.success("RAG pipeline is ready!")

st.header("Ask a Question")

if Question := st.chat_input("Type your question here..."):
    if st.session_state.rag_ready:
        result = ask_question(st.session_state.vector_store, st.session_state.prompt, st.session_state.llm, Question)
        st.session_state.messages.append({"role": "user", "content": Question})
        st.session_state.messages.append({"role": "assistant", "content": result["answer"]})
        
        st.chat_message("user").write(Question)
        st.chat_message("assistant").write(result["answer"])

    else:
        st.warning("Please upload PDF files to initialize the RAG pipeline.")



