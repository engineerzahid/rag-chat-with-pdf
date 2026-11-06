from rag.loader import pdf_loader
from rag.chunker import chunker
from rag.embeddings import embeddings_model
from rag.vector_store import vector_store,document_search
from rag.config import TOKEN_K


file_path = "company.pdf"

documents = pdf_loader(file_path)
chunks = chunker(documents)

embeddding_model = embeddings_model()

vector_store_result =  vector_store(chunks,embeddding_model)

print("Vector store process completed successfully")
print("totlal chunks",len(chunks))


question = "what does zahid labs do?"


search_results = document_search(vector_store_result,question,k=TOKEN_K)

print("question: ",question)


for document in search_results:

    print("-"*60)
    print("source",document.metadata.get("source"))
    print("page",document.metadata.get("page",0)+1)
    print("content",document.page_content)
