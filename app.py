import streamlit as st
from pytube import YouTube
from googletrans import Translator
from gtts import gTTS
import tempfile

st.title("🌍 YouTube Video Translator with Speaker")

url = st.text_input("🎬 YouTube Video Link")

lang = st.selectbox("🌐 اپنی زبان منتخب کریں:", ["ur", "hi", "en"])

if url:
    try:
        yt = YouTube(url)
        st.video(url)

        if "en" in yt.captions:
            caption = yt.captions["en"]
            subtitle_text = caption.generate_srt_captions()

            st.subheader("📄 Original Subtitles")
            st.text_area("English Subtitles", subtitle_text, height=200)

            translator = Translator()
            translated = translator.translate(subtitle_text, dest=lang).text

            st.subheader("🌍 Translated Subtitles")
            st.text_area("Translated", translated, height=200)

            tts = gTTS(translated, lang=lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)
                st.audio(tmp_file.name, format="audio/mp3")
        else:
            st.error("❌ اس ویڈیو میں English Subtitles موجود نہیں ہیں۔")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
