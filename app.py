
import streamlit as st
from rag.pipeline import create_rag_pipeline, ask_question

st.set_page_config(
    page_title="RAG QA System",
    page_icon=":books:"
)

st.title("RAG QA System")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_ready" not in st.session_state:
    st.session_state.rag_ready = False


# Sidebar: Upload PDF
with st.sidebar:

    st.title("Upload PDF Document")

    uploaded_files = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="pdf_uploader",
        accept_multiple_files=True
    )

    if st.button("Process Files"):

        if uploaded_files:

            files_path = []

            try:
                with st.spinner("Processing files..."):

                    for uploaded_file in uploaded_files:

                        with open(uploaded_file.name, "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        files_path.append(uploaded_file.name)

                    vector_store, prompt, llm = create_rag_pipeline(files_path)

                    st.session_state.vector_store = vector_store
                    st.session_state.prompt = prompt
                    st.session_state.llm = llm

                    st.session_state.rag_ready = True

                st.success("Files processed successfully!")

            except Exception as e:
                st.session_state.rag_ready = False
                st.error(f"Processing Error: {str(e)}")

        else:
            st.warning("Please upload at least one PDF file.")


# Chat Section
st.header("Ask Questions about the Document")


# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat Input
if QUESTION := st.chat_input("Ask a question about the document"):

    if not st.session_state.rag_ready:

        st.warning("Please upload and process a PDF first.")

    else:

        # Save User Question
        st.session_state.messages.append({
            "role": "user",
            "content": QUESTION
        })

        with st.chat_message("user"):
            st.markdown(QUESTION)

        # Generate Assistant Answer
        with st.chat_message("assistant"):

            with st.spinner("Finding your answer..."):

                try:
                    result = ask_question(
                        st.session_state.vector_store,
                        st.session_state.prompt,
                        st.session_state.llm,
                        QUESTION
                    )

                    answer = result["answer"]

                    st.markdown(answer)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })

                except Exception as e:

                    st.error(f"Question Error: {str(e)}")
