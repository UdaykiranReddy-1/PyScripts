"""
Spell Guard module

This module provides functions for spell checking and proofreading text.
"""

import lmproof as lm

def correct_text(text: str) -> str:
    """
    Correct spelling and grammar in the given text.
    
    Args:
        text (str): The text to be corrected
        
    Returns:
        str: The corrected text
    """
    proof = lm.load("en")
    corrected_text = proof.proofread(text)
    return corrected_text

def check_spelling(text: str) -> list:
    """
    Check spelling in the given text and return a list of errors.
    
    Args:
        text (str): The text to check
        
    Returns:
        list: List of spelling errors found in the text
    """
    proof = lm.load("en")
    errors = proof.check(text)
    return errors
