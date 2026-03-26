# 🔊 TTS Studio - Text-to-Speech Converter

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square&logo=streamlit)
![gTTS](https://img.shields.io/badge/gTTS-Google_TTS-yellow?style=flat-square)
![Languages](https://img.shields.io/badge/Languages-10+-green?style=flat-square)

A feature-rich **Text-to-Speech Studio** built with Python and Streamlit. Convert any text to natural-sounding audio using Google Text-to-Speech (gTTS), with multi-language support and audio download.

## 🚀 Features

- 🌍 **10+ Languages**: English (US/UK), Hindi, Telugu, Spanish, French, German, Japanese, Chinese
- ⏰ **Speed Control**: Normal and slow speech modes
- 📥 **Audio Download**: Save generated audio as MP3
- 🎵 **Live Preview**: Play audio directly in browser
- 📝 **Sample Texts**: Pre-loaded example texts for quick demo
- 📊 **Stats Dashboard**: Character count, word count, language info

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| TTS Engine | gTTS (Google Text-to-Speech) |
| Audio | Python io.BytesIO |
| Language | Python 3.10+ |

## 💻 Installation

```bash
git clone https://github.com/Arawn-D/tts-studio.git
cd tts-studio
pip install -r requirements.txt
streamlit run app.py
```

## 🏃 Usage

1. Run `streamlit run app.py`
2. Select your preferred language in the sidebar
3. Toggle slow speech if needed
4. Type or paste text in the main area
5. Click **Convert to Speech**
6. Preview audio and download as MP3

## 🌍 Supported Languages

| Language | Code |
|----------|------|
| English (US) | en |
| English (UK) | en-uk |
| Hindi | hi |
| Telugu | te |
| Spanish | es |
| French | fr |
| German | de |
| Japanese | ja |
| Chinese | zh-CN |

## 💡 Key Concepts Demonstrated

- **gTTS Integration**: Google TTS API for natural speech synthesis
- **Audio Streaming**: In-memory audio handling with BytesIO
- **Multi-language NLP**: Unicode text processing for different scripts
- **Streamlit Components**: Audio player, download buttons, metrics

## 👨‍💻 Author

**Vijay Dokka** - Python Developer | AI/ML Engineer
- GitHub: [@Arawn-D](https://github.com/Arawn-D)
- Email: helloaavijay@gmail.com

---

> Built with ❤️ using gTTS + Streamlit
