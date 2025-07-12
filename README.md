# AI Doctor 2.0 – Voice and Vision

**Multimodal AI Diagnostic Assistant Powered by Voice, Vision, and Transformer Intelligence**
<img width="2842" height="1642" alt="Interface" src="https://github.com/user-attachments/assets/950a8d97-6556-4209-a882-d1522ea94c1c" />

---

## 📌 Project Description

**AI Doctor 2.0** is a fully local, real-time medical triage system that simulates a digital doctor. It combines **speech input**, **visual symptom analysis**, and **transformer-based reasoning** to provide a **probable diagnosis**, a **confidence score**, and a **natural-sounding voice response** — all in under 3 seconds.

This project explores the intersection of **natural language processing**, **computer vision**, and **multimodal AI**, delivering a practical tool for preliminary health screening and patient interaction.

---

## 🧰 Tech Stack & Tools

| Layer                    | Technology Used                                      |
| ------------------------ | ---------------------------------------------------- |
| **Voice Input (STT)**    | OpenAI Whisper (local model)                         |
| **Image Processing**     | LLaMA 3 Vision via GROQ API                          |
| **Multimodal Reasoning** | Custom fusion logic using Transformer architecture   |
| **Voice Output (TTS)**   | ElevenLabs API (primary), gTTS (fallback)            |
| **Interface**            | Gradio + Flask                                       |
| **Others**               | OpenCV, FFmpeg, PyAudio, requests, SpeechRecognition |

---

## 💡 Key Features

* Accepts both **voice and image** input for symptom description.
* Converts speech to text using **Whisper** with high medical term accuracy (\~95%).
* Processes uploaded images via **LLaMA 3 Vision** to extract visual embeddings.
* Combines both modalities using a **custom transformer-like fusion** system.
* Generates real-time **diagnostic output** in both **text** and **doctor-like voice** using **ElevenLabs**.
* Runs completely **locally** with minimal external dependencies (excluding APIs).

---

## ⚙️ Workflow

```
Patient voice input  ➜  Whisper STT  
                     ➜  Symptom transcript  

Patient image input  ➜  OpenCV + LLaMA 3 Vision  
                     ➜  1024-dim image embedding  

Voice + Image        ➜  Fusion via custom transformer logic  
                     ➜  Diagnosis + Confidence + Recommendation  

Diagnosis Text       ➜  ElevenLabs/gTTS  
                     ➜  Natural speech output (Doctor's voice)  
```

---

## 📊 System Performance (Summary)

| Metric                               | Result              |
| ------------------------------------ | ------------------- |
| Speech-to-Text Accuracy              | 95% (medical terms) |
| Image Inference Time                 | \~0.8 seconds       |
| Diagnosis Accuracy (vs expert cases) | 92%                 |
| End-to-End Latency                   | 2.8 seconds         |
| Voice Output Quality (MOS)           | 4.5 / 5             |
| Usability Score (SUS)                | 80 / 100            |

---

## 🖥️ Repository Structure

```
ai-doctor-2.0-voice-and-vision/
├── app.py                      # Entry point: Flask + Gradio
├── services/
│   ├── voice_of_doctor_input.py  # Records & transcribes speech (Whisper)
│   ├── voice_of_patient.py       # Handles image input & sends to LLaMA 3 Vision
│   └── brain_of_doc.py           # Multimodal reasoning logic
├── tts_output.py               # TTS response using ElevenLabs/gTTS
├── ui.py                       # Gradio frontend
├── requirements.txt            # Dependencies
└── tests/                      # Unit tests
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AIwithhassan/ai-doctor-2.0-voice-and-vision.git
cd ai-doctor-2.0-voice-and-vision
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Then open your browser at `http://localhost:7860`

---

## 🔍 Use Cases & Applications

* Preliminary health screening in remote or low-resource settings
* AI health assistant for educational or triage purposes
* Accessible digital healthcare tool for the elderly or visually impaired
* Research in multimodal fusion and transformer-based reasoning in healthcare

---

## 📌 Future Enhancements

* Multilingual speech support
* Medicine recommendation system
* Integration with EHR systems
* Android/iOS frontend deployment
* Offline fallback for vision model using open-source alternatives

---

## 📖 License

This project is intended for educational and research use only.
All clinical results are **non-diagnostic** and should not be used as a substitute for professional medical advice.

---

#📩 Contact
For feedback, collaboration, suggestions, or opportunities to improve and expand this project, feel free to reach out:

Abdullah Imran
Email: abdullahimran017@gmail.com
LinkedIn: linkedin.com/in/abdullah-imran-211658230
