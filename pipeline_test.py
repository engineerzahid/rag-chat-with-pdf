from rag.pipeline import create_rag_pipeline,ask_question

question = "What services zahid labs provide?"

files_path = ["company.pdf"]

vector_store,prompt,llm = create_rag_pipeline(files_path)

result =  ask_question(vector_store,prompt,llm,question)

print("\n Question")
print(question)


print("\n Answer:")
print(result["answer"])


for source in result["sources"]:

    print("-"*40)

    print("source",source["source"])
    print("page",source["page"])
    print("content",source["content"])


    
