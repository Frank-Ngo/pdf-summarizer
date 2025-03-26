# 📄 Smart PDF Summarizer with Auto-Tagging

This tool extracts text from uploaded PDF documents and uses GPT-3.5 to:
- Generate a concise summary
- Auto-tag the document with key topics

### 🚀 Features
- Streamlit interface (no HTML needed)
- LLM-powered summarization
- Auto-tagging with GPT
- Clean file upload + secure API usage via `.env`

### 📦 Installation

```bash
pip install -r requirements.txt
```

### 🧠 Usage
```bash
streamlit run pdf_summarizer.py
```

### 🔒 Environment Variables
Create a .env file with your OpenAI key:

```ini
OPENAI_API_KEY=your-key-here
```

