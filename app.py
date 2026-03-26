import streamlit as st
from gtts import gTTS
import io
import base64
import os
import tempfile

st.set_page_config(
    page_title="TTS Studio",
    page_icon="🔊",
    layout="wide"
)

st.title("🔊 Text-to-Speech Studio")
st.markdown("**Convert any text to natural-sounding audio using gTTS (Google Text-to-Speech)**")

with st.sidebar:
    st.header("⚙️ Settings")
    language = st.selectbox(
        "Language",
        options=[
            ("English (US)", "en"),
            ("English (UK)", "en-uk"),
            ("Hindi", "hi"),
            ("Telugu", "te"),
            ("Spanish", "es"),
            ("French", "fr"),
            ("German", "de"),
            ("Japanese", "ja"),
            ("Chinese", "zh-CN"),
        ],
        format_func=lambda x: x[0]
    )
    slow_mode = st.checkbox("Slow speech", value=False)
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    - 🌍 10+ languages
    - ⏰ Slow/normal speed
    - 📥 Download audio
    - 🔄 Real-time preview
    """)
    st.markdown("---")
    st.markdown("Built by **Vijay Dokka** | [GitHub](https://github.com/Arawn-D)")


col1, col2 = st.columns([2, 1])

with col1:
    text_input = st.text_area(
        "Enter your text here:",
        height=200,
        placeholder="Type or paste any text here to convert to speech...",
        max_chars=5000
    )
    char_count = len(text_input)
    st.caption(f"{char_count}/5000 characters")

    col_btn1, col_btn2 = st.columns(2)
    convert_btn = col_btn1.button("🔊 Convert to Speech", type="primary", use_container_width=True)
    clear_btn = col_btn2.button("🗑️ Clear", use_container_width=True)

with col2:
    st.markdown("### Sample Texts")
    samples = {
        "Intro": "Hello! I am Vijay Dokka, a Python developer specializing in AI and Machine Learning.",
        "Tech": "Artificial Intelligence is transforming the world through deep learning and neural networks.",
        "Quote": "The only way to do great work is to love what you do. - Steve Jobs"
    }
    for label, sample in samples.items():
        if st.button(f"📝 {label}", use_container_width=True):
            st.session_state["sample_text"] = sample
            st.rerun()

if "sample_text" in st.session_state:
    text_input = st.session_state["sample_text"]

if clear_btn:
    st.session_state.pop("sample_text", None)
    st.rerun()

if convert_btn:
    if not text_input.strip():
        st.warning("Please enter some text to convert!")
    else:
        with st.spinner("Generating audio..."):
            try:
                lang_code = language[1]
                tts = gTTS(text=text_input, lang=lang_code, slow=slow_mode)

                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)
                audio_bytes = audio_buffer.read()

                st.success("✅ Audio generated successfully!")

                st.markdown("### 🎵 Preview")
                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="📥 Download MP3",
                    data=audio_bytes,
                    file_name="tts_output.mp3",
                    mime="audio/mp3",
                    use_container_width=True
                )

                st.markdown("### 📊 Stats")
                col_s1, col_s2, col_s3 = st.columns(3)
                col_s1.metric("Characters", len(text_input))
                col_s2.metric("Words", len(text_input.split()))
                col_s3.metric("Language", language[0].split()[0])

            except Exception as e:
                st.error(f"Error generating speech: {str(e)}")
