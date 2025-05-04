"""
Audio Book module

This module provides functions to convert PDF documents to audio books using text-to-speech.
"""

import PyPDF2
import pyttsx3

def create_audio_book(pdf_path: str, output_path: str = 'output.mp3') -> None:
    """
    Convert a PDF document to an audio book using text-to-speech.
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str): Path to save the output audio file (default: 'output.mp3')
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            readpdf = PyPDF2.PdfReader(file)
            
            # Initialize text-to-speech engine
            speaker = pyttsx3.init()
            
            # Set speech properties
            speaker.setProperty('rate', 200)  # speaking rate
            speaker.setProperty('volume', 1)  # volume level
            
            # Get and set a different voice
            voices = speaker.getProperty('voices')
            for voice in voices:
                if "english" in voice.name.lower() and "us" in voice.name.lower():
                    speaker.setProperty('voice', voice.id)
                    break
            
            text = ""
            # Extract text from each page
            for pagenumber in range(len(readpdf.pages)):
                page = readpdf.pages[pagenumber]
                text += page.extract_text()
            
            # Save the text as audio
            speaker.save_to_file(text, output_path)
            speaker.runAndWait()

            print(f"✅ Successfully created audio book: {output_path}")
            
            # Cleanup
            speaker.stop()
            
    except Exception as e:
        raise Exception(f"Error creating audio book: {str(e)}")
