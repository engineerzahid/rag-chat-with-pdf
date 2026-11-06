from rag.loader import pdf_loader


file_path = "company.pdf"

documetns = pdf_loader(file_path)

for index,document in enumerate(documetns):

    print("index",index+1)
    print("content",document.page_content)
    print("source",document.metadata.get('source'))
