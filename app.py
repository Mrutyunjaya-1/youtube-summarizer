import streamlit as st
from utils import *

st.title("🎥 YouTube Summarizer (Gemini AI)")
st.caption("Paste any YouTube video link and generate a summary + article")
url = st.text_input("Enter YouTube URL")
if st.button("Generate"):

    if not url:
        st.warning("Please enter a YouTube URL")
    else:
        video_id = extract_video_id(url)
        text = get_transcript(video_id)

        if "not available" in text.lower():
            st.error(text)
        else:
            with st.spinner("Processing..."):
                summary = summarize_text(text)
                article = generate_article(summary)

            st.subheader("Summary")
            st.write(summary)

            st.subheader("Article")
            st.markdown(article)

            st.download_button(
                label="Download Article",
                data=article,
                file_name="article.md",
                mime="text/markdown"
            )