from rag.groq_model import get_llm


llm = get_llm()

result = llm.invoke("what is Rag define in two paragraphs")

print("result",result.content)