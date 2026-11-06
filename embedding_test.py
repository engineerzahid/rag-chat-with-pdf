from rag.chunker import chunker
from rag.loader import pdf_loader
from rag.embeddings import embeddings_model

file_path = "company.pdf"

documents = pdf_loader(file_path)
chunks = chunker(documents)
embdmodel = embeddings_model()

for index, chunk in enumerate(chunks):
    print("index",index+1)
    print("chunk_data",chunk.page_content)
    print("source",chunk.metadata.get('source'))

    text = chunk.page_content

    embeddings = embdmodel.embed_query(text)

    print("embeddings",embeddings)

