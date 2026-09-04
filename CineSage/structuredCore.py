import os
from dotenv import load_dotenv

# from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from pydantic import BaseModel
from typing import List , Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)



llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=1000
)
model = ChatHuggingFace( llm=llm)
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
     Extract movie information from the paragraph 
     {format_instructions}
     
     """),
     ("human", "{paragraph}")
     ]
)

para = input("Give your paragraph ")
print("1. Paragraph received")
final_prompt = prompt.invoke(
    {"paragraph": para,
     "format_instructions": parser.get_format_instructions()}
)
print("2. Prompt created")
print(final_prompt)

print("3. Sending request to Hugging Face...")
response = model.invoke(final_prompt)
print("4. Response received")
movie = parser.parse(response.content)

print(movie)


