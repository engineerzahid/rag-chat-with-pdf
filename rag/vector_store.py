from langchain_community.vectorstores import FAISS


def create_vector_store(chunks,embeddings):

    results = FAISS.from_documents(documents=chunks,embedding=embeddings)

    return results


def document_search(vector_store,question,k=4):

     results = vector_store.similarity_search(
         question,k
         )


     return results