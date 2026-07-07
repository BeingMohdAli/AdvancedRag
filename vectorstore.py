from dotenv import load_dotenv
load_dotenv()
import chromadb
from langchain_mistralai import MistralAIEmbeddings
embeddings = MistralAIEmbeddings(model="mistral-embed")
from langchain_core.documents import Document

docs = [
    Document(
        page_content="Artificial intelligence is transforming the world.",
        metadata={"source": "article1.txt", "page": 1}
    ),
    Document(
        page_content="Machine learning is a subset of artificial intelligence.",
        metadata={"source": "article2.txt", "page": 1}
    ),
    Document(
        page_content="Deep learning uses neural networks with many layers.",
        metadata={"source": "article3.txt", "page": 1}
    ),
    Document(
        page_content="Natural language processing helps computers understand human language.",
        metadata={"source": "article4.txt", "page": 1}
    ),
    Document(
        page_content="Python is the most popular language for AI and machine learning.",
        metadata={"source": "article5.txt", "page": 1}
    ),
]
from langchain_chroma import Chroma
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="AR",
    collection_name="Rag"
)

retreiver = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs = {"k":1}
)
result= retreiver.invoke("what is deep learning")
for d in result:
    print(d.page_content)
    print("*"*30)