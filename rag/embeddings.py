from langchain_huggingface import HuggingFaceEmbeddings
from rag.config import EMBEDDING_MODEL


def embeddings_model():

	model = HuggingFaceEmbeddings(
		model_name = EMBEDDING_MODEL
		)

	return model

