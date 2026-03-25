from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Extract video ID
def extract_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]
    elif "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    else:
        return url


# Get transcript
def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()

        transcript_list = api.list(video_id)

        # Try English
        try:
            transcript = transcript_list.find_transcript(['en'])
        except:
            # Fallback to any available language
            transcript = transcript_list.find_transcript(
                [t.language_code for t in transcript_list]
            )

        fetched = transcript.fetch()
        return " ".join([t.text for t in fetched])

    except Exception as e:
        return f"Transcript not available. Error: {str(e)}"


# Summarize
def summarize_text(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
            You are an expert content summarizer.

            Summarize this YouTube transcript:

            - Keep it concise
            - Highlight key ideas
            - Remove repetition
            - Make it easy to read

            Transcript:
            {text[:3000]}
            """
        )
        return response.text
    except Exception as e:
        return f"Summarization failed: {str(e)}"


# Generate article
def generate_article(summary):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
            You are a professional blog writer.

            Convert this into a high-quality article:

            - Catchy Title
            - Engaging Introduction
            - Key Takeaways (bullet points)
            - Detailed Explanation
            - Real-world relevance
            - Conclusion

            Make it engaging and human-like.

            Summary:
            {summary}
            """
        )
        return response.text
    except Exception as e:
        return f"Article generation failed: {str(e)}"