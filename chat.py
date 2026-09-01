import langchain
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    api_key=os.getenv("MISTRAL_API_KEY")
)

response = model.invoke("Explain what is useState hook in react.")

print(response.content)