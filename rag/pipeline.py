from rag import vector_store
from rag import prompt
from rag.loader import pdf_loader
from rag.chunker import chunker
from rag.embeddings import embeddings_model
from rag.prompt import create_prompt
from rag.vector_store import create_vector_store,document_search
from rag.groq_model import get_llm
from rag.config import TOKEN_K

def create_rag_pipeline(files_path):
    all_documents = []

    for file_path in files_path:
        documents = pdf_loader(file_path)
        all_documents.extend(documents)

    chunks = chunker(all_documents)

    embd = embeddings_model()

    vector_store = create_vector_store(chunks, embd)

    prompt = create_prompt()
    llm = get_llm()

    return vector_store, prompt, llm



def ask_question(vector_store,prompt,llm,question):

    
    results = document_search(vector_store,question,TOKEN_K)

    context = "\n\n".join(
        document.page_content for document in results
        )

    message = prompt.format_messages(
        context = context,
        question = question
        )

    answer = llm.invoke(message)


    source = [
        {
            "source": result.metadata.get("source"),
            "page": result.metadata.get("page",0)+1,
            "content": result.page_content
            
            }
        
        for result in results
        ]
   

    return {
        "answer": answer.content,
        "sources": source
        }
        
       



