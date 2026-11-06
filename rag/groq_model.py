from langchain_groq import ChatGroq
from rag.config import GROQ_API_KEY,GROQ_MODEL


def get_llm():

    llm = ChatGroq(api_key=GROQ_API_KEY,model=GROQ_MODEL)


    return llm