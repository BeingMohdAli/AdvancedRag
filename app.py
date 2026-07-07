# from dotenv import load_dotenv
# load_dotenv()
# from langchain_mistralai import ChatMistralAI

# llm = ChatMistralAI(
#     model="mistral-large-latest"
#     )


import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="Advancved RAG")


# Define text documents
documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
]

# Define a query text
query = "Hello World"