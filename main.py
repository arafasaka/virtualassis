from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from time import ctime  # get time details
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import logging
import webbrowser
import ctypes

# import wolframalpha
import smtplib
import wikipedia
import random
from urllib.request import urlopen
import json
from googletrans import Translator
from gtts import gTTS
import playsound
import operator
import eel

eel.init('web')


##FUNCTION

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


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

@eel.expose
def coba():
    text = get_audio()
    return text

@eel.expose
def get_audio():
    global said
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


def authenticate_google():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("calendar", "v3", credentials=creds)

    return service


def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=date.isoformat(),
            timeMax=end_date.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        speak("No upcoming events found.")
    else:
        speak(f"You have {len(events)} events on this day.")

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "am"
            else:
                start_time = (
                    str(int(start_time.split(":")[0]) - 12) + start_time.split(":")[1]
                )
                start_time = start_time + "pm"

            speak(event["summary"] + " at " + start_time)


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year + 1

    if month == -1 and day != -1:
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)


def notename(text):
    date = datetime.datetime.now()
    file_name = note_name + ".txt"

def note(text):
    file_name = note_name + ".txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])

def search(text):
    search_term = text.split("for")[-1]
    url = f"https://google.com/search?q={search_term}"
    webbrowser.get().open(url)
    speak(f"Here is what I found for {search_term} on google")

def shownotes(text):
    file = open(notes_term +".txt", "r") 
    subprocess.Popen(["notepad.exe", notes_term +".txt"])
    #speak(file.read(6))    


def youtube(text):
    search_term = text.split("youtube")[-1]
    url = f"https://www.youtube.com/results?search_query={search_term}"
    webbrowser.get().open(url)
    speak(f"Here is what I found for {search_term} on youtube")


def chrome(text):
    chrome = "C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
    subprocess.Popen([chrome])


def location(text):
    url = f"http://maps.google.com/?q={search_term}"
    webbrowser.get().open(url)
    speak(f"Here is the location for {search_term} on google maps")


##VARIABLE


WAKE = "hello"
THANKS = "thank you"
NAME = "what is your name"
HOW = "how are you"
LOVE = "love"
SORRY = "sorry"

SERVICE = authenticate_google()


@eel.expose
def asking():
    global search_term, note_name, note_text, notes_term
    print("Start")
    speak("ready")
    while True:
    
        print("Listening")
        text = get_audio()
       

        if text.count(WAKE) > 0:
            speak("What can i do Mr. arafasaka")
            text = get_audio()
            
            

            CALENDAR_STRS = ["what do i have", "do i have plans", "my shedule"]
            for phrase in CALENDAR_STRS:
                if phrase in text:

                    date = get_date(text)
                    if date:
                        get_events(date, SERVICE)
                    else:
                        speak("I don't understand")

            NOTE_STRS = ["make a note", "write this down", "remember this"]
            for phrase in NOTE_STRS:
                if phrase in text:
                    speak("What would you like me to name this note?")
                    note_name = get_audio()
                    notename(note_name)
                    speak("What would you like me to write down?")
                    note_text = get_audio()
                    note(note_text)
                    speak("I've made a note of that.")

            CHROME_STRS = ["find something"]
            for phrase in CHROME_STRS:
                if phrase in text:
                    chrome(text)
                    speak("I've open it for you")

            TIME_STRS = ["what's the time", "tell me the time", "what time is it"]
            for phrase in TIME_STRS:
                if phrase in text:
                    speak("Sir, the time is " + ctime())
                    print(ctime())
                    # time = ctime().split(" ")[3].split(":")[0:2]
                    # if time[0] == "00":
                    #     hours = '12'
                    # else:
                    #     hours = time[0]
                    # minutes = time[1]
                    # time = f'{hours} {minutes}'
                    # speak(time)
                    # print("Now is " + f'{hours} : {minutes}')

            QUIT_STRS = ["quit", "exit", "go offline", "leave me alone"]
            for phrase in QUIT_STRS:
                if phrase in text:
                    speak("going offline")
                    print("Going Offline")
                    exit()

            SEARCH_STRS = ["search for", "looking for"]
            for phrase in SEARCH_STRS:
                if phrase in text:
                    search(text)

            SHOWNOTE_STRS = ["check my notes", "open my notes"]
            for phrase in SHOWNOTE_STRS:
                if phrase in text:
                    speak("What notes would you like to open?")
                    notes_term = get_audio()
                    shownotes(text)

            YOUTUBE_STRS = ["in youtube", "on youtube", "open youtube", "search on youtube"]
            for phrase in YOUTUBE_STRS:
                if phrase in text:
                    youtube(text)

            LOCATION_STRS = ["find location"]
            for phrase in LOCATION_STRS:
                if phrase in text:
                    speak("whats the location?")
                    search_term = get_audio()
                    location(text)
                    

            CALC_STRS = ["please calculate"]
            for phrase in CALC_STRS:
                if phrase in text:
                    try:
                        speak("Say what you want to calculate, example: 3 plus 3")
                        #calculate(text)
                        text1 = get_audio()
                        calculate = (text1)
                        print("ready")
                        def get_operator_fn(op):
                            return {
                            '+' : operator.add,
                            '-' : operator.sub,
                            'x' : operator.mul,
                            'divided' :operator.__truediv__,
                            'Mod' : operator.mod,
                            'mod' : operator.mod,
                            '^' : operator.xor,
                            }[op]
                        def eval_binary_expr(op1, oper, op2):
                            op1,op2 = int(op1), int(op2)
                            return get_operator_fn(oper)(op1, op2)
                        print(eval_binary_expr(*(text1.split())))
                        speak("The answer is")
                        speak(eval_binary_expr(*(text1.split())))
                    except Exception as e:
                        speak("Sorry i didn't get that, anything else?")
                    

            WIKI_STRS = ["wikipedia"]
            for phrase in WIKI_STRS:
                if phrase in text:
                    try:
                        speak("Searching Wikipedia...")
                        text = text.replace("wikipedia", "")
                        results = wikipedia.summary(text, sentences=3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                        speak("That's all i got sir")
                    except Exception as e:
                        speak("Sorry i didn't get that, anything else?")
                        print("Exception: " + str(e))

            MUSIC_STRS = ["play music", "give my mood back", "play some music"]
            for phrase in MUSIC_STRS:
                if phrase in text:
                    speak("Here you go with music")
                    # music_dir = "G:\\Song"
                    music_dir = "C:\\Users\\User\\Music\\music\\"
                    songs = os.listdir(music_dir)
                    print(songs)
                    random = os.startfile(os.path.join(music_dir, songs[1]))

            TRANS_STRS = ["translate to indonesian"]
            for phrase in TRANS_STRS:
                if phrase in text:
                    try:
                        translator = Translator()
                        search_term = text.split("indonesian")[-1]
                        speak(f"Here is what I know for {search_term}")
                        translated_sentence = translator.translate(
                            search_term, src="en", dest="id"
                        )
                        print(translated_sentence.text)
                        speak_indo(translated_sentence.text)
                    except Exception as e: 
                        print(e)
                        speak("Sorry i didn't get that, anything else?")
                        break

            TRANSJA_STRS = ["translate to japanese"]
            for phrase in TRANSJA_STRS:
                if phrase in text:
                    try:
                        translator = Translator()
                        search_term = text.split("japanese")[-1]
                        speak(f"Here is what I know for {search_term}")
                        translated_sentence = translator.translate(
                            search_term, src="en", dest="ja"
                        )
                        print(translated_sentence.text)
                        speak_ja(translated_sentence.text)
                    except:
                        speak("Sorry i didn't get that, anything else?")
                        break
                        pass

            POWERLOCK_STRS = ["lock window"]
            for phrase in POWERLOCK_STRS:
                if phrase in text:
                    try:
                        speak("locking the device")
                        ctypes.windll.user32.LockWorkStation()
                    except:
                        speak("Sorry i didn't get that, anything else?")
                        break
                        pass

            POWERHIBER_STRS = ["go to hibernate"]
            for phrase in POWERHIBER_STRS:
                if phrase in text:
                    try:
                        speak("Device is going to hibernate")
                        subprocess.call("shutdown / h")
                    except:
                        speak("Sorry i didn't get that, anything else?")
                        break
                        pass

            NEWS_STRS = [
                "what's the news today",
                "news of the day",
                "give me some news",
                "news today",
            ]
            for phrase in NEWS_STRS:
                if phrase in text:
                    try:
                        jsonObj = urlopen(
                            "http://newsapi.org/v2/everything?domains=detik.com&apiKey=fd7b9b4313e64abcba2426b73fcd0fe2"
                        )
                        data = json.load(jsonObj)
                        i = 1

                        speak_indo("ini dia berita yang dilansir dari detik.com")
                        print("""=============== DETIK  ============""" + "\n")
                        for item in data["articles"]:
                            if i == 6:
                                pass
                            else:
                                print(str(i) + ". " + item["title"] + "\n")
                                print(item["description"] + "\n")
                                speak_indo(str(i) + ". ")
                                speak_indo(item["title"] + "\n")
                                i += 1
                    except Exception as e:
                        print(str(e))
                        break

        elif text.count(THANKS):
            speak("as you wish")

        elif text.count(NAME):
            speak("You can call me jarvis, mr. ara gave me that name")

        elif text.count(HOW):
            speak("Im fine, how about you sir?")

        elif text.count(LOVE):
            speak("You now i dont have heart sir, dont test me")

        elif text.count(SORRY):
            speak("it's okay, but if i can punch you, i'll do it sir")
    
       
        
        #pass
    

eel.start('index.html', size=(400,600), port=8001)
