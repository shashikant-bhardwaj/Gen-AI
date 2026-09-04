import streamlit as st
import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

from pydantic import BaseModel
from typing import List, Optional
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

model = ChatHuggingFace(llm=llm)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Extract movie information from the paragraph.

        {format_instructions}
        """
    ),
    ("human", "{paragraph}")
])


# ---------------- Streamlit UI ----------------

st.title("🎬 CineSage")

st.write("Extract useful information from a movie paragraph.")

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250
)

if st.button("Extract Information"):

    if paragraph:

        final_prompt = prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })

        response = model.invoke(final_prompt)

        movie = parser.parse(response.content)

        st.subheader("Movie Information")

        st.write("**Title:**", movie.title)

        st.write("**Release Year:**", movie.release_year)

        st.write("**Genre:**", ", ".join(movie.genre))

        st.write("**Director:**", movie.director)

        st.write("**Cast:**", ", ".join(movie.cast))

        st.write("**Rating:**", movie.rating)

        st.write("**Summary:**", movie.summary)

    else:
        st.write("Please enter a movie paragraph.")