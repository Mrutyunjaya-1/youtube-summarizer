import requests
import os
from google import genai
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
    url = "https://youtube-transcriptor.p.rapidapi.com/transcript"

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "youtube-transcriptor.p.rapidapi.com"
    }

    querystring = {"video_id": video_id}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # 🔥 Correct extraction
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("transcriptionAsText", "Transcript not found.")

        return "Transcript not available."

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
