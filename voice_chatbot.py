
import speech_recognition as sr
from gtts import gTTS
import os

# دیکشنری اختصاصی کلمات
word_definitions = {
    "سلام": "درود و احوالپرسی",
    "خداحافظ": "خداحافظی کردن",
    "پایتون": "یک زبان برنامه نویسی سطح بالا",
    "هوش مصنوعی": "شاخه ای از علوم کامپیوتر برای ساخت ماشین های هوشمند",
    "برنامه نویسی": "فرایند ساخت برنامه های کامپیوتری"
}

def text_to_speech(text):
    tts = gTTS(text=text, lang='fa')
    tts.save("output.mp3")
    os.system("start output.mp3")

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("در حال گوش دادن...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language='fa-IR')
        print(f"شما گفتید: {text}")
        return text
    except:
        return None

def main():
    while True:
        user_input = speech_to_text()
        
        if user_input:
            if user_input.lower() in ["خروج", "بستن"]:
                text_to_speech("خداحافظ! تا بعدی")
                break
                
            definition = word_definitions.get(user_input, "این کلمه در دیکشنری موجود نیست")
            print(f"تعریف: {definition}")
            text_to_speech(definition)
        else:
            text_to_speech("متوجه صحبت شما نشدم")

if __name__ == "__main__":
    main()
