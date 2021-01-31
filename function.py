import datetime
import time as timeout
from time import ctime  # get time details
import pytz #timezone
import subprocess
import webbrowser
import config_apikey_weather
from bs4 import BeautifulSoup #getlocation
import requests
import eel #gui
import operator #operator matematika
import smtplib #system quit dll
import wikipedia #wikpedia
import random #mengacak data
import json 
from googletrans import Translator # translator
from urllib.request import urlopen #buka url
from audio_handler import *
from auth_handler import *

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

response = requests.get("https://official-joke-api.appspot.com/random_joke")
setup_joke = response.json()['setup']
punchline_joke = response.json()['punchline']


@eel.expose
def nama_greet(data):
    global nama
    nama = data

def greet():
    hour = int(datetime.datetime.now().hour)
    try:
        if hour >= 0 and hour <= 12:
            speak(f"Good Morning {nama}")
            print(f"Good Morning {nama}!")
            eel.computer(f"Good Morning {nama}!")
        elif hour > 12 and hour < 16:
            speak(f"Good Afternoon {nama}!")
            print(f"Good Afternoon {nama}!")
            eel.computer(f"Good Afternoon {nama}!")
        else:
            speak(f"Good Evening {nama}!")
            print(f"Good Evening {nama}!")
            eel.computer(f"Good Evening {nama}!")
    except:
        if hour >= 0 and hour <= 12:
            speak("Good Morning")
            print("Good Morning!")
            eel.computer("Good Morning!")
        elif hour > 12 and hour < 16:
            speak("Good Afternoon!")
            print("Good Afternoon!")
            eel.computer("Good Afternoon!")
        else:
            speak("Good Evening!")
            print("Good Evening!")
            eel.computer("Good Evening!")


def hello():
    try:
        eel.computer(f"How can i help you {nama} ?")
        speak(f"How can i help you {nama} ?")
    except:
        eel.computer(f"How can i help you?")
        speak(f"How can i help you?")

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
        eel.computer("No upcoming events found.")
        speak("No upcoming events found.")
    else:
        eel.computer(f"You have {len(events)} events on this day.")
        speak(f"You have {len(events)} events on this day.")

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
            eel.computer(start, event["summary"])
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

def time():
    eel.computer(ctime())
    try:
        speak(f"{nama}, the time is " + ctime())
    except:
        speak("Sir, the time is " + ctime())    
    print(ctime())

def files(text):
    eel.computer("Sure, is it word, excel, or power point?")
    speak("Sure, is it word, excel, or power point?")
    files_term = get_audio()
    eel.human(files_term)

    eel.computer("could you please tell me the name of the file?")
    speak("could you please tell me the name of the file?")
    filename_term = get_audio()
    eel.human(filename_term)

    if files_term == "document" or files_term == "word document":
        wordi(filename_term)
    elif files_term == "excel" or files_term == "excel document":
        excel(filename_term)
    elif files_term == "powerpoint" or files_term == "powerpoint document" or files_term == "power point":
        ppt(filename_term)
    else:
        eel.computer("I'm, sorry i didn't get that")
        speak("I'm, sorry i didn't get that")
        
def word(text_word):
    filename = text_word + ".docx"
    result = []
    for root, dir, files in os.walk("C:\\Users"):
        if filename in files:
            result.append(os.path.join(root, filename))
            os.startfile(os.path.join(root, filename))
    if result == []:
        try:
            speak(f"Sorry i can't find your document {nama}")
            eel.computer(f"Sorry i can't find your document {nama}")
        except:
            speak("Sorry i can't find your document")
            eel.computer("Sorry i can't find your document")
            print("tidak ditemukan exel")
    else:
        print(result)
        eel.computer(result)
        speak(f"I've open it for you {nama}")

def excel(text_excel):
    filename = text_excel + ".xlsx"
    result = []
    for root, dir, files in os.walk("C:\\Users"):
        if filename in files:
            result.append(os.path.join(root, filename))
            os.startfile(os.path.join(root, filename))
    if result == []:
        try:
            speak(f"Sorry i can't find your document {nama}")
            eel.computer(f"Sorry i can't find your document {nama}")
        except:
            speak("Sorry i can't find your document")
            eel.computer("Sorry i can't find your document")
            print("tidak ditemukan exel")
    else:
        print(result)
        eel.computer(result)
        speak(f"I've open it for you {nama}")

def ppt(text_ppt):
    filename = text_ppt + ".pptx"
    result = []
    for root, dir, files in os.walk("C:\\Users"):
        if filename in files:
            result.append(os.path.join(root, filename))
            os.startfile(os.path.join(root, filename))
    if result == []:
        try:
            speak(f"Sorry i can't find your document {nama}")
            eel.computer(f"Sorry i can't find your document {nama}")
        except:
            speak("Sorry i can't find your document")
            eel.computer("Sorry i can't find your document")
            print("tidak ditemukan exel")

    else:
        print(result)
        eel.computer(result)
        speak(f"I've open it for you {nama}")
   

def calculate(text1):
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
    eel.computer(eval_binary_expr(*(text1.split())))
    speak("The answer is")
    speak(eval_binary_expr(*(text1.split()))) 

def location(search_term):
    url = f"http://maps.google.com/?q={search_term}"
    webbrowser.get().open(url)
    eel.computer(f"Here is the location for {search_term} on google maps")
    speak(f"Here is the location for {search_term} on google maps")

def search(text):
    search_term = text.split("for")[-1]
    url = f"https://google.com/search?q={search_term}"
    webbrowser.get().open(url)
    eel.computer(f"Here is what I found for {search_term} on google")
    speak(f"Here is what I found for {search_term} on google")

def youtube(text):
    search_term = text.split("youtube")[-1]
    url = f"https://www.youtube.com/results?search_query={search_term}"
    webbrowser.get().open(url)
    eel.computer(f"Here is what I found for {search_term} on youtube")
    speak(f"Here is what I found for {search_term} on youtube")

def onlinestore(text):
    search_term = text.split("of")[-1]
    eel.computer("Let me check sir, do you prefer tokopedia or shopee?")
    speak("Let me check sir, do you prefer tokopedia or shopee?")
    store_term = get_audio()
    eel.human(store_term)
    if store_term == "tokopedia":
        tokopedia(search_term)
    elif store_term == "shopee":
        shopee(search_term)
    else:
        eel.computer("I'm, sorry i didn't get that")
        speak("I'm, sorry i didn't get that")

def tokopedia(text):
    search_term = text.split("tokopedia")[-1]
    url = f"https://www.tokopedia.com/search?st=product&q={search_term}"
    webbrowser.get().open(url)
    eel.computer(f"Here is what I found for {search_term} on tokopedia")
    speak(f"Here is what I found for {search_term} on tokopedia")

def shopee(text):
    search_term = text.split("shopee")[-1]
    url = f"https://shopee.co.id/search?keyword={search_term}"
    webbrowser.get().open(url)
    eel.computer(f"Here is what I found for {search_term} on shopee")
    speak(f"Here is what I found for {search_term} on shopee")

def shownotes(notes_term):
    # file = open(notes_term +".txt", "r") 
    #subprocess.Popen(["notepad.exe", notes_term +".txt"])
    subprocess.Popen(["notepad.exe", os.path.expanduser('~\\Documents\\notes'+ notes_term)])
    #speak(file.read(6))

def notename(note_name):
    global file_name
    file_name = note_name + ".txt"

def note(note_text):
    #file_name = note_name + ".txt"
    # with open(file_name, "w") as f:
    #     f.write(note_text)
    notes_path = os.path.expanduser('~\\Documents\\notes')
    if not os.path.exists(os.path.expanduser('~\\Documents\\notes')):
        os.makedirs(notes_path)
        with open(os.path.join(os.path.expanduser('~'),'Documents\\notes',file_name), "w") as f:
            f.write(note_text)
        subprocess.Popen(["notepad.exe", os.path.expanduser('~\\Documents\\notes\\'+ file_name)])
    else:
        with open(os.path.join(os.path.expanduser('~'),'Documents\\notes',file_name), "w") as f:
            f.write(note_text)
        subprocess.Popen(["notepad.exe", os.path.expanduser('~\\Documents\\notes\\'+ file_name)])

def chrome(text):
    url = "https://google.com/"
    webbrowser.get().open(url)

def wiki(text):
    try:
        eel.computer("Searching Wikipedia...")
        speak("Searching Wikipedia...")
        text = text.replace("wikipedia", "")
        results = wikipedia.summary(text, sentences=3)
        eel.computer("According to Wikipedia")
        speak("According to Wikipedia")
        eel.computer(results)
        print(results)
        speak(results)
        speak("That's all i got sir")
    except Exception as e:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")
        print("Exception: " + str(e))    


def music():
    try:
        eel.computer("Here you go with music")
        speak("Here you go with music")
        music_dir = os.path.expanduser('~\\Music\\')
        songs = os.listdir(music_dir)
        music = random.choice(songs)
        print(songs)
        os.startfile(os.path.join(music_dir, music))
    except Exception as e:
        print(e)
        eel.computer("Im sorry something wrong with your directory")
        speak("Im sorry something wrong with your directory")
        

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
URL = ''

def translateindo(text):
    try:
        translator = Translator()
        search_term = text.split("indonesian")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="id"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_indo(translated_sentence.text)
    except Exception as e: 
        print(e)
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def translatejapan(text):
    try:
        translator = Translator()
        search_term = text.split("japanese")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="ja"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_ja(translated_sentence.text)
    except:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def translatezh(text):
    try:
        translator = Translator()
        search_term = text.split("mandarin")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="zh-CN"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_zh(translated_sentence.text)
    except:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def translatees(text):
    try:
        translator = Translator()
        search_term = text.split("spanish")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="es"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_es(translated_sentence.text)
    except:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def translatefr(text):
    try:
        translator = Translator()
        search_term = text.split("french")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="fr"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_fr(translated_sentence.text)
    except:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def translatehi(text):
    try:
        translator = Translator()
        search_term = text.split("hindi")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="hi"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_hi(translated_sentence.text)
    except:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def translatear(text):
    try:
        translator = Translator()
        search_term = text.split("arabic")[-1]
        eel.computer(f"Here is what I know for {search_term}")
        speak(f"Here is what I know for {search_term}")
        translated_sentence = translator.translate(
            search_term, src="en", dest="ar"
        )
        eel.computer(translated_sentence.text)
        print(translated_sentence.text)
        speak_ar(translated_sentence.text)
    except:
        eel.computer("Sorry i didn't get that, anything else?")
        speak("Sorry i didn't get that, anything else?")

def get_location():
    global latitude, longitude
    try:
        URL = 'https://iplocation.com/'
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        city = soup.find(class_='city').get_text()
        country = soup.find(class_='country_name').get_text()
        latitude = soup.find(class_='lat').get_text()
        longitude = soup.find(class_='lng').get_text()
        # print(longitude, latitude)
        return city, country, latitude, longitude
        
    except Exception as e:
        print(str(e))
        speak('Error, location could not be retrieved')    

def weather(latitude, longitude):
    try:
        api_key = config_apikey_weather.api_key
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        complete_url = base_url + "lat=" + \
            str(latitude) + "&lon=" + str(longitude) + "&appid=" + api_key
        response = requests.get(complete_url)
        x = response.json()
        temp = (int)((x["main"]["temp"]) - 273.15)
        feel = (int)((x["main"]["feels_like"]) - 273.15)
        sunrise = x["sys"]["sunrise"]
        sunrise = datetime.datetime.fromtimestamp(
            sunrise).strftime('%H:%M')
        sunset = x["sys"]["sunset"]
        sunset = datetime.datetime.fromtimestamp(
            sunset).strftime('%H:%M')
        description = x["weather"][0]["description"]
        print(f'The temperature is {temp}°C and it feels like {feel} °C\nThe predicted forecast is {description}')
        eel.computer(f'The temperature is {temp}°C and it feels like {feel} °C\nThe predicted forecast is {description}')
        speak(f'The temperature is {temp} degrees celsius. It feels like {feel} degrees celsius. The predicted forecast is {description}')
    except Exception as e:
        print(str(e))
        eel.computer("An error occurred while retrieving weather information")
        print("An error occurred while retrieving weather information")
        speak("An error occurred while retrieving weather information")
    if x["cod"] != "404":
        return x
    else:
        return False    

def news():
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
                break
            else:
                eel.computer(str(i) + ". " + item["title"] + "\n")
                print(str(i) + ". " + item["title"] + "\n")
                # eel.computer(item["description"] + "\n")
                print(item["description"] + "\n")
                speak_indo(str(i) + ". ")
                speak_indo(item["title"] + "\n")
                i += 1
    except Exception as e:
        print(e)
        eel.computer("For now i don't know sir, would you want me to open news website?")
        speak("For now i don't know sir, would you want me to open news website?")


def joke():
    print(setup_joke)
    eel.computer(setup_joke)
    speak(setup_joke)
    timeout.sleep(5)
    print(punchline_joke)
    eel.computer(punchline_joke)
    speak(punchline_joke)
