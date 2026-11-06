from langchain_core.prompts import ChatPromptTemplate


def create_prompt():

    template = ChatPromptTemplate.from_template(
        """
        You are document question-answering assistant
        Ony answer the question if context is given
        If answer is not found in documents then simply reply required information not found in your uploaded documents.

        DO not add facts


        Context
        {context}


        Question
        {question}


        Answer:

        """
        )

    return template