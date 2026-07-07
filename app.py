# from dotenv import load_dotenv
# load_dotenv()
# from langchain_mistralai import ChatMistralAI

# llm = ChatMistralAI(
#     model="mistral-large-latest"
#     )


import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="Advancved RAG")
