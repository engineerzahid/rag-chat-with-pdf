from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def pdf_loader(file_path:str):

    pdf_load = PyPDFLoader(file_path)

    documents = pdf_load.load()

    source_name = Path(file_path).name

    for document in documents:
        document.metadata['source']= source_name


    return documents 