from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-large-latest"
    )

print(llm.invoke("How r you "))