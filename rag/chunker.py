from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.config import CHUNK_OVERLAP,CHUNK_SIZE


def chunker(documents):
    
    chunk_data = RecursiveCharacterTextSplitter(
                      chunk_size = CHUNK_SIZE,
                      chunk_overlap = CHUNK_OVERLAP
                      )

    chunks = chunk_data.split_documents(documents)


    return chunks