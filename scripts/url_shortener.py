"""
URL Shortener module

This module provides functions to shorten URLs using TinyURL service.
"""

import pyshorteners

def shorten_url(long_url: str) -> str:
    """
    Shorten a given URL using TinyURL service.
    
    Args:
        long_url (str): The original long URL to be shortened
        
    Returns:
        str: The shortened URL
    """
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(long_url)
        print(f"✅ Successful")
        return short_url
    except Exception as e:
        raise Exception(f"❌ Error shortening URL: {str(e)}")
