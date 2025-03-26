import fitz  # PyMuPDF
import openai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_and_tag(text):
    prompt = f"""You are an assistant that summarizes PDF documents.

Summarize the following content in under 200 words, and provide 3 to 5 key topic tags.

Content:
{text[:3000]}

Respond in this format:
Summary: ...
Tags: ...
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


st.title("📄 Smart PDF Summarizer with Auto-Tagging")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading and summarizing..."):
        text = extract_text_from_pdf(uploaded_file)
        result = summarize_and_tag(text)

    st.success("Done!")

    if "Tags:" in result:
        summary, tags = result.split("Tags:")
        st.markdown("---")

        st.markdown("### 📝 Summary")
        st.write(summary.strip())
        
        st.markdown("---")
        st.markdown("### 🏷️ Tags")
        
        for tag in tags.strip().split(","):
            st.markdown(f"- {tag.strip()}")

        st.markdown("---")

        # ✅ Download only if parsing worked
        download_text = f"Summary:\n{summary.strip()}\n\nTags:\n{tags.strip()}"

        st.download_button("💾 Download Summary", data=download_text, file_name="summary.txt")
    else:
        st.write(result)



