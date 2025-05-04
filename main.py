from scripts import (
    # audio_book,
    # data_faker,
    # generate_qr,
    # notifier,
    # remove_bg,
    spell_guard,
    # summariser,
    # url_shortener,
    # youtube_transcript,

)

def main():
    # Welcome to the PyScripts main interface!
    # Please uncomment and modify the function calls below to use specific features.
    
    # Audio Book
    # audio_book.create_audio_book("AI_article.pdf", "output.mp3")
    
    # Data Faker
    # fake_data = data_faker.generate_fake_data(10)
    # print(fake_data)
    
    # Generate QR Code
    # generate_qr.create_qr_code("https://example.com", "qr_code.png")
    
    # Notifier
    # notifier.create_reminder("Reminder", "This is a test reminder", 0.5)
    
    # Remove Background
    # remove_bg.remove_background("input.png", "output.png")
    
    # Spell Guard
    corrected_text = spell_guard.correct_text("Ths is a tset")
    print(corrected_text)
    
    # Summariser
    # Use case 1 (Scraping Webpage and Summarizing)
    # webpage_url = "https://www.learncpp.com/cpp-tutorial/unsigned-integers-and-why-to-avoid-them/" ## Sample URL for Testing The Script
    # webpage_text = summariser.scrape_web_content(webpage_url)

    # if webpage_text:
    #     summary = summariser.summarize_text(webpage_text)
    #     print("Summarized Article:")
    #     print(summary)
    # else:
    #     print("Webpage scraping failed.")

    # Use case 2 (Summarizing Text)
    # text = """Long text here"""
    # summary = summariser.summarize_text(text)
    # print("Summarized Text:")
    # print(summary)
    
    # URL Shortener
    # short_url = url_shortener.shorten_url("https://example.com")
    # print(short_url)
    
    # YouTube Transcript
    # transcript = youtube_transcript.get_transcript("video_id")
    

if __name__ == "__main__":
    main()
