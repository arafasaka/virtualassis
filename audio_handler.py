from gtts import gTTS #google text to speech
import playsound #bantu dalam sound
import pyttsx3
import speech_recognition as sr
import os

def speak(text):
    engine = pyttsx3.init()
    # engine.setProperty('voice', '')
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts = gTTS(text=text, lang="en")
#     filename = "voice.mp3"
#     tts.save(filename)
#     playsound.playsound(filename)
#     os.remove(filename)


def speak_indo(text_indo):
    tts = gTTS(text=text_indo, lang="id")
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_ja(text_ja):
    tts = gTTS(text=text_ja, lang="ja")
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_es(text_es):
    tts = gTTS(text=text_es, lang="es")
    filename = "voice3.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_fr(text_fr):
    tts = gTTS(text=text_fr, lang="fr")
    filename = "voice4.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_hi(text_hi):
    tts = gTTS(text=text_hi, lang="hi")
    filename = "voice5.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_ar(text_ar):
    tts = gTTS(text=text_ar, lang="ar")
    filename = "voice6.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_zh(text_zh):
    tts = gTTS(text=text_zh, lang="zh-CN")
    filename = "voice7.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()