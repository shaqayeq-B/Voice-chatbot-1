# Voice-chatbot-1
It is a small part of the AI chatbot project 
```markdown
# 📖 Smart Voice Dictionary

A speech recognition-based chatbot dictionary with text-to-speech capabilities for Persian language

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10.0-green)

## 🚀 Key Features
- Voice input through microphone
- Artificial voice responses
- Expandable Persian dictionary
- Voice control commands
- Cross-platform compatibility (Windows/Linux)

## 📦 Requirements
### Essential Libraries
```bash
pip install SpeechRecognition gtts pyaudio
```

### Hardware Requirements
- Functional microphone
- Speakers/headphones

## 🛠️ Installation
1. Clone repository:
```bash
git clone https://github.com/yourusername/voice-dictionary.git
```

2. Navigate to project directory:
```bash
cd voice-dictionary
```

3. Run main script:
```bash
python main.py
```

## 🎮 How to Use
1. Speak into microphone when program is running
2. Clearly pronounce words to get definitions
3. Control commands:
   - "خروج" or "بستن" (exit/close) to terminate
4. System will respond with audio feedback

## ➕ Adding New Words
Edit `main.py` and update the dictionary:
```python
word_definitions["New Word"] = "Custom Definition"
```

## ⚠️ Limitations
- Requires internet connection for speech recognition
- Performance depends on microphone quality
- Basic starter dictionary

## 🔮 Future Development
- [ ] Integrate official dictionary API
- [ ] Add GUI interface
- [ ] Add English language support
- [ ] Implement auto-learning system
- [ ] Search history storage

## 📜 License
Released under [MIT]
