import os
from dotenv import load_dotenv

# from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint



load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
model = ChatHuggingFace( llm=llm)
prompt = ChatPromptTemplate.from_messages([
    ("system",
"""
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean readable format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""
),
     ("human",
     "Extract structured movie information from the following paragraph:\n\n{paragraph}")
     ]
)

para = input("Give your paragraph ")
final_prompt = prompt.invoke(
    {"paragraph": para}
)
response = model.invoke(final_prompt)

print(response.content)