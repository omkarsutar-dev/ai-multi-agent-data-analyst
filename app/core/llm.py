from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv() # Automatically loads OPENAI_API_KEY from .env


def get_llm():
    return ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"  # cost-efficient
    )