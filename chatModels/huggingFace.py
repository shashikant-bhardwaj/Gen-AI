import os
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace( llm=llm)
response = model.invoke("who are  you?")

print(response.content)