"""
YouTube Transcript module

This module provides functions to fetch and format YouTube video transcripts.
"""

from youtube_transcript_api import YouTubeTranscriptApi

def clean_text(text: str) -> str:
    """
    Clean the text by removing unwanted characters and normalizing spaces.
    
    Args:
        text (str): The text to clean
        
    Returns:
        str: Cleaned text
    """
    # Replace non-breaking spaces and newline with regular spaces
    text = text.replace("\xa0\n", " ")
    # Replace multiple spaces with a single space
    text = " ".join(text.split())
    return text

def fetch_transcript(video_id: str, output_file: str = "transcript.txt") -> str:
    """
    Fetch YouTube video transcript and save it to a file.
    
    Args:
        video_id (str): YouTube video ID. The URL of any youtube video that we watch will be something like below --
            https://www.youtube.com/watch?v=xXxXxXxXxXx
            videoId is the 11 digit code after `?v=`
        output_file (str): Path to save the formatted transcript
        
    Returns:
        str: The formatted transcript text
        
    Raises:
        Exception: If there's an error fetching or processing the transcript
    """
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Collect all lines of the transcript
        lines = [line['text'] for line in transcript]
        
        # Clean and join all lines into a single string
        full_text = clean_text(" ".join(lines))
        
        # Split the text into sentences
        sentences = full_text.split(". ")
        
        # Initialize formatted text
        formatted_text = ""
        sentence_counter = 0
        
        # Build the formatted text
        for sentence in sentences:
            formatted_text += sentence.strip()
            if not sentence.endswith("."):
                formatted_text += "."
            
            sentence_counter += 1
            
            # Add a new paragraph after every 3 sentences
            if sentence_counter % 3 == 0:
                formatted_text += "\n\n"
            else:
                formatted_text += " "

        # Save to file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_text.strip())
            
        print(f"✅ Transcript successfully written to {output_file}")
        
    except Exception as e:
        raise Exception(f"Error fetching transcript: {str(e)}")
