from youtube_transcript_api import YouTubeTranscriptApi

def clean_text(text):
    """Cleans the text by removing unwanted characters and normalizing spaces."""
    # Replace non-breaking spaces and newline with regular spaces
    text = text.replace("\xa0\n", " ")
    # Replace multiple spaces with a single space
    text = " ".join(text.split())

    return text

def fetch_and_format_transcript(video_id, output_file="ytranscript.txt"):
    """Fetches the transcript and outputs formatted text to a file"""
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Collect all lines of the transcript
        lines = [line['text'] for line in transcript]
        
        # Clean and join all lines into a single string
        full_text = clean_text(" ".join(lines))
        
        # Split the text into sentences based on periods
        sentences = full_text.split(". ")

        '''Formatting is done by splitting a whole paragraph into paragraphs with 3 periods'''
        
        # Initialize formatted text
        formatted_text = ""
        sentence_counter = 0
        
        # Build the text with the specified formatting
        for sentence in sentences:
            # Add the sentence with a period (if it doesn't already end with one)
            formatted_text += sentence.strip()
            if not sentence.endswith("."):
                formatted_text += "."
            
            # Increment the sentence counter
            sentence_counter += 1
            
            # Add a new paragraph after every 3 sentences
            if sentence_counter % 3 == 0:
                formatted_text += "\n\n"
            else:
                formatted_text += " "

        # Write the formatted text to a file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_text.strip())

        print(f"Transcript successfully written to {output_file} with the desired formatting.")
    except Exception as e:
        print(f"An error occurred: {e}")

# The URL of any youtube video that we watch will be something like below --
# https://www.youtube.com/watch?v=xXxXxXxXxXx
# videoId is the 11 digit code after `?v=`
# Place the videoId of the video that we want to extract the transcript of in the below variable..

# Video ID of the YouTube video
video_id = "xXxXxXxXxXx"

# Call the function
fetch_and_format_transcript(video_id)
