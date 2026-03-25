import gradio as gr
from utils import *
import requests


def get_video_details(video_id):
    url = f"https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v={video_id}&format=json"
    try:
        res = requests.get(url).json()
        return res.get("title"), res.get("thumbnail_url")
    except:
        return "YouTube Video", None


def process(url):
    if not url:
        return None, "", "Please enter URL", ""

    video_id = extract_video_id(url)

    title, thumbnail = get_video_details(video_id)
    text = get_transcript(video_id)

    if "not available" in text.lower():
        return thumbnail, title, text, ""

    summary = summarize_text(text)
    article = generate_article(summary)

    return thumbnail, title, summary, article


def save_markdown(article):
    file_path = "article.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(article)
    return file_path


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎥 YouTube → Article Generator (GenAI)")
    gr.Markdown("Convert YouTube videos into summaries and structured articles (Markdown)")

    with gr.Row():
        url = gr.Textbox(label="Enter YouTube URL", scale=4)
        btn = gr.Button("Generate", variant="primary")

    thumbnail = gr.Image(label="Thumbnail")
    title = gr.Textbox(label="Video Title")

    summary = gr.Textbox(label="Summary", lines=8)

    # 🔥 Markdown Output
    article = gr.Markdown(label="Generated Article")

    download_btn = gr.File(label="Download Article (.md)")

    btn.click(
        process,
        inputs=url,
        outputs=[thumbnail, title, summary, article]
    )

    article.change(
        save_markdown,
        inputs=article,
        outputs=download_btn
    )

demo.launch()
