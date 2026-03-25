# 🎥 YouTube Summarizer (GenAI Project)

A Generative AI application that converts YouTube videos into **concise summaries** and **structured article-style content** using the Gemini API.

---

## 🚀 Features

* 🔗 Extract transcript from YouTube videos (via RapidAPI)
* ✨ Generate concise summaries using Gemini AI
* 📝 Convert summaries into structured blog articles
* 🌐 Deployed on Hugging Face Spaces (Gradio)
* ⚡ Simple and interactive UI

---

## 🧠 Tech Stack

* **Frontend**: Gradio
* **Backend**: Python
* **LLM**: Google Gemini API (`google-genai`)
* **API Integration**: RapidAPI (YouTube Transcript)
* **Deployment**: Hugging Face Spaces

---

## 📁 Project Structure

```
youtube-summarizer/
│
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set Environment Variables

Create a `.env` file (for local use):

```
GEMINI_API_KEY=your_gemini_api_key
RAPIDAPI_KEY=your_rapidapi_key
```

---

### 4️⃣ Run Application

```bash
python app.py
```

---

## 🌍 Live Demo

👉 https://huggingface.co/spaces/mrutyunjaya-03/youtube-summarizer

---

## ⚠️ Notes

* Some YouTube videos may not provide transcripts.
* API rate limits may apply depending on your plan.
* Songs or music videos may generate lyric-based summaries.

---

## 💡 Future Improvements

* 🎬 Show video thumbnail & title
* 📋 Copy-to-clipboard feature
* 📄 Export article as PDF
* 🌐 Multi-language support

---

## 👨‍💻 Author

**Mrutyunjaya Debata**

* 🔗 LinkedIn: https://www.linkedin.com/in/mrutyunjaya3806debata/
* 💻 GitHub: https://github.com/Mrutyunjaya-1

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
