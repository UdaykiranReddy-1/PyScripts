"""
Summariser module

This module provides functions for text summarization using BART model and web scraping.
"""

from transformers import BartForConditionalGeneration, BartTokenizer
import requests
from bs4 import BeautifulSoup

def summarize_text(text: str, max_length: int = 150, min_length: int = 50) -> str:
    """
    Summarize the given text using BART model.
    
    Args:
        text (str): The text to be summarized
        max_length (int): Maximum length of the summary
        min_length (int): Minimum length of the summary
        
    Returns:
        str: The summarized text
    """
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    inputs = tokenizer.encode(
        "summarize: " + text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )
    
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def scrape_web_content(url: str) -> str:
    """
    Scrape content from a webpage.
    
    Args:
        url (str): URL of the webpage to scrape
        
    Returns:
        str: The scraped content as text
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text(separator='\n', strip=True)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error scraping webpage: {str(e)}")
