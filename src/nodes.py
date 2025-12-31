import os
import requests
from bs4 import BeautifulSoup
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.output_parsers import JsonOutputParser

# Initialize Search and Utilities
search = GoogleSerperAPIWrapper()

def web_search_node(state):
    """
    Scrapes the web to find context for obscure merchants.
    """
    question = state["question"]
    # Optimize query for Llama 3
    search_query = f"what business is {question} and what do they sell"
    
    results = search.results(search_query)
    urls = [x['link'] for x in results['organic'][:3]] # Top 3 links
    
    context = ""
    for url in urls:
        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.content, "html.parser")
            context += " ".join([p.get_text() for p in soup.find_all("p")[:3]])
        except:
            continue
            
    return {"context": context[:2000]} # Limit context window

def categorization_node(state):
    """
    The final classification logic.
    """
    # This uses the CATEGORY_PROMPT defined in prompts.py
    # and invokes the llama3_json model
    return {"generation": classification_result}
