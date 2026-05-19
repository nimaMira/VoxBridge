# VoxBridge

**A voice-first AI assistant designed for inclusive and human-centered interaction.**

VoxBridge is a personal open-source project exploring how voice can become the primary
bridge between humans and AI — especially for people who struggle with traditional
keyboard-and-screen interfaces.

---

## Mission

VoxBridge is built around three core goals:

### 1. Accessibility
Making AI usable for people who are excluded by traditional interfaces — blind and
visually impaired users, the elderly, people with limited technical literacy, and
users whose first language is not the one the software was designed for.

### 2. Human-Centered Interaction
Building a deeper, more natural conversation between humans and machines: emotional
awareness, empathy, personalization through learning, and a genuinely conversational
rather than transactional experience.

### 3. Voice-Driven Productivity
Enabling hands-free interaction with the local system — speaker identification, voice
commands, and file operations through natural spoken language.

---

## Current Status

This project is in early development (v0.1). The current focus is the basic
speech → AI → speech loop. See the Roadmap below for the planned evolution.

---

## Roadmap

| Version | Focus | Status |
|---------|-------|--------|
| v0.1 | Basic voice loop: speech-to-text → LLM → text-to-speech | In progress |
| v0.2 | Persistent conversation memory and user personalization | Planned |
| v0.3 | Speaker recognition (who is talking) | Planned |
| v0.4 | Emotion and tone analysis from voice | Planned |
| v1.0 | Local file operations through voice commands | Planned |
| v2.0 | Multimodal extension (visual input) | Future |

---

## Tech Stack

- **Language:** Python 3.10+
- **Speech-to-Text:** [OpenAI Whisper](https://github.com/openai/whisper) (local, open source)
- **Text-to-Speech:** `pyttsx3` (offline) — planned upgrade to Coqui TTS
- **AI Backend:** OpenAI API or [Ollama](https://ollama.ai) for local LLM inference
- **Audio I/O:** `sounddevice`, `numpy`
- **Configuration:** `python-dotenv`, `pydantic`

---

## Quick Start

### Prerequisites

- Python 3.10 or higher
- A working microphone and speakers
- Either an OpenAI API key **or** [Ollama](https://ollama.ai) installed locally

### Installation

```bash
# Clone the repository
git clone https://github.com/nimaMira/VoxBridge.git
cd VoxBridge

# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Copy the example environment file and add your credentials:

```bash
cp .env.example .env
# Then edit .env in your favorite editor
```

### Run

```bash
python src/main.py
```

---

## Project Structure

```
VoxBridge/
├── src/
│   ├── main.py              # Entry point — main interaction loop
│   ├── speech_to_text.py    # Whisper-based audio transcription
│   ├── text_to_speech.py    # TTS output
│   ├── ai_engine.py         # LLM communication layer
│   └── config.py            # Configuration management
├── tests/                   # Unit tests
├── docs/                    # Architecture and design documents
├── examples/                # Sample scripts and usage demos
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment configuration
├── .gitignore
├── LICENSE
└── README.md
```

---

## Contributing

VoxBridge is a personal learning project, but contributions and feedback are very
welcome — especially in these areas:

- **Accessibility testing** with screen-reader users
- **Localization** for additional languages (currently targeting English, German, Persian)
- **Audio quality** improvements
- **Documentation** and examples

If you want to contribute, please open an issue first to discuss your idea.

---

## License

MIT License — see the [LICENSE](LICENSE) file for the full text.

---

## Author

**Nima HamedIman**
Aspiring Application Developer in vocational retraining (Fachinformatiker für
Anwendungsentwicklung) at CBW Hamburg.

- GitHub: [@nimaMira](https://github.com/nimaMira)
- Focus areas: Cybersecurity, Artificial Intelligence, Linux

---

## Acknowledgments

- The OpenAI Whisper team for open-sourcing high-quality speech recognition
- The accessibility advocacy community for the inspiration behind this project
