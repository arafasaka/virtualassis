from function import *
eel.init('web')

##ASKING FUNCTION

WAKE = "hello"
THANKS = "thank you" 
THANKS2 = "thanks" 
NAME = "your name"
HOW = "how are you"
HOW2 = "what's up"
LOVE = "love"
SORRY = "sorry"
HELP = "what can you do"
HELP2 = "you can do"

@eel.expose
def Asking():
    global search_term, note_name, note_text, notes_term, text1
    print("Start")
    speak("ready")
    greet()
    while True:
    
        print("Listening")
        eel.computer("Listening..")
        text = get_audio()
        eel.human(text)
        
        if text.count(WAKE) > 0:
            hello()
            text = get_audio()
            eel.human(text)

           
            CALENDAR_STRS = ["what do i have", "do i have plans", "my shedule"]
            for phrase in CALENDAR_STRS:
                if phrase in text:
                    date = get_date(text)
                    if date:
                        SERVICE = authenticate_google()
                        get_events(date, SERVICE)
                    else:
                        eel.computer("I don't understand")
                        speak("I don't understand")

            NOTE_STRS = ["make a note", "write this down", "remember this"]
            for phrase in NOTE_STRS:
                if phrase in text:
                    eel.computer("What would you like me to name this note?")
                    speak("What would you like me to name this note?")
                    note_name = get_audio()
                    eel.human(note_name)
                    notename(note_name)
                    eel.computer("What would you like me to write down?")
                    speak("What would you like me to write down?")
                    note_text = get_audio()
                    note(note_text)
                    eel.computer("I've made a note of that.")
                    speak("I've made a note of that.")

            SHOWNOTE_STRS = ["check my notes", "open my notes", "check my note"]
            for phrase in SHOWNOTE_STRS:
                if phrase in text:
                    try:
                        eel.computer("What notes would you like to open?")
                        speak("What notes would you like to open?")
                        notes_term = get_audio()
                        shownotes(notes_term)
                    except Exception as e:
                        eel.computer(f"Sorry i couldn't find the note called {notes_term}, anything else?")
                        speak(f"Sorry i couldn't find the note called {notes_term}, anything else?")
                    break
                    
            CHROME_STRS = ["find something"]
            for phrase in CHROME_STRS:
                if phrase in text:
                    chrome(text)
                    eel.computer("I've open it for you")
                    speak("I've open it for you")

            FILES_STRS = ["find my document", "Open my document", "Open my file", "find my file"]
            for phrase in FILES_STRS:
                if phrase in text:
                    try:
                        files(text)
                    except Exception as e:
                        print(e)

            TIME_STRS = ["what's the time", "tell me the time", "time is it", "what tell me the time"]
            for phrase in TIME_STRS:
                if phrase in text:
                    time()
                    break
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
                    eel.computer("going offline")
                    speak("going offline")
                    print("Going Offline")
                    exit()

            SEARCH_STRS = ["search for", "looking for"]
            for phrase in SEARCH_STRS:
                if phrase in text:
                    search(text)

            YOUTUBE_STRS = ["in youtube", "on youtube", "open youtube", "search on youtube"]
            for phrase in YOUTUBE_STRS:
                if phrase in text:
                    youtube(text)
                    break

            ONLINESTORE_STRS = ["the price of", "price of"]
            for phrase in ONLINESTORE_STRS:
                if phrase in text:
                    onlinestore(text)
                    break

            TOKOPEDIA_STRS = ["in tokopedia", "on tokopedia", "open tokopedia", "search on tokopedia"]
            for phrase in TOKOPEDIA_STRS:
                if phrase in text:
                    tokopedia(text)
                    break

            SHOPEE_STRS = ["in shopee", "on shopee", "open shopee", "search on shopee", "on shopie"]
            for phrase in SHOPEE_STRS:
                if phrase in text:
                    shopee(text)
                    break

            LOCATION_STRS = ["find location"]
            for phrase in LOCATION_STRS:
                if phrase in text:
                    eel.computer("whats the location?")
                    speak("whats the location?")
                    search_term = get_audio()
                    location(search_term)
                    

            CALC_STRS = ["please calculate", "can you calculate this", "i want to calculate", "solve this"]
            for phrase in CALC_STRS:
                if phrase in text:
                    try:
                        eel.computer("Say what you want to calculate, example: 3 plus 3")
                        speak("Say what you want to calculate, example: 3 plus 3")
                        text1 = get_audio()
                        calculate(text1)
                        print("ready")
                    except Exception as e:
                        speak("Sorry i didn't get that, anything else?")
                    

            WIKI_STRS = ["wikipedia"]
            for phrase in WIKI_STRS:
                if phrase in text:
                    wiki(text)

            MUSIC_STRS = ["play music", "give my mood back", "play some music"]
            for phrase in MUSIC_STRS:
                if phrase in text:
                    music()

            TRANS_STRS = ["translate to indonesian"]
            for phrase in TRANS_STRS:
                if phrase in text:
                        translateindo(text)

            TRANSJA_STRS = ["translate to japanese"]
            for phrase in TRANSJA_STRS:
                if phrase in text:
                        translatejapan(text)

            TRANSHI_STRS = ["translate to hindi"]
            for phrase in TRANSHI_STRS:
                if phrase in text:
                        translatehi(text)

            TRANSZH_STRS = ["translate to mandarin"]
            for phrase in TRANSZH_STRS:
                if phrase in text:
                        translatezh(text)

            TRANSES_STRS = ["translate to spanish"]
            for phrase in TRANSES_STRS:
                if phrase in text:
                        translatees(text)

            TRANSFR_STRS = ["translate to french"]
            for phrase in TRANSFR_STRS:
                if phrase in text:
                        translatefr(text)

            TRANSAR_STRS = ["translate to arabic"]
            for phrase in TRANSAR_STRS:
                if phrase in text:
                        translatear(text)

            POWERLOCK_STRS = ["lock window" "lock the window"]
            for phrase in POWERLOCK_STRS:
                if phrase in text:
                    try:
                        speak("locking the device")
                        ctypes.windll.user32.LockWorkStation()
                    except:
                        eel.computer("Sorry i didn't get that, anything else?")
                        speak("Sorry i didn't get that, anything else?")
                        break
                        pass

            POWERHIBER_STRS = ["go to hibernate"]
            for phrase in POWERHIBER_STRS:
                if phrase in text:
                    try:
                        eel.computer("Device is going to hibernate")
                        speak("Device is going to hibernate")
                        subprocess.call("shutdown / h")
                    except:
                        eel.computer("Sorry i didn't get that, anything else?")
                        speak("Sorry i didn't get that, anything else?")
                        break
                        pass

            JOKE_STRS = ["give me a joke", "something funny", "gime me some jokes"]
            for phrase in JOKE_STRS:
                if phrase in text:
                    try:
                        joke()
                    except Exception as e:
                        print(e)
                        eel.computer("Sorry, i'm not in the mood")
                        speak("Sorry, i'm not in the mood")

            WEATHER_STRS = ["weather like today"]
            for phrase in WEATHER_STRS:
                if phrase in text:
                    try:
                        city, country, latitude, longitude = get_location()
                        weather(latitude, longitude)
                    except Exception as e:
                        eel.computer("Sorry, I can't get the detail right now")
                        print("Sorry, I can't get the detail right now")
                        speak("Sorry, I can't get the detail right now")
                        break

            NEWS_STRS = ["what's the news today","news of the day","give me some news"]
            for phrase in NEWS_STRS:
                if phrase in text:
                    news()


        elif text == THANKS or text == THANKS2:
            eel.computer("as you wish")
            speak("as you wish")

        elif text == NAME:
            eel.computer("You can call me jarvis, mr. ara gave me that name")
            speak("You can call me jarvis, mr. ara gave me that name")

        elif text == HOW or text == HOW2:
            eel.computer("Im fine, how about you sir?")
            speak("Im fine, how about you sir?")    

        elif text == LOVE:
            eel.computer("You now i dont have heart sir, dont test me")
            speak("You now i dont have heart sir, dont test me")
            
        elif text == SORRY:
            eel.computer("it's okay, im here for you")
            speak("it's okay, i'm here for you")
            
        elif text == HELP or text == HELP2:
            eel.computer("i can do anything. Just say the keyword")
            speak("i can do anything. Just say the keyword")
            
            eel.computer("would you like me to open the tutorial how to command me?")
            speak("would you like me to open the tutorial how to command me?")
            text = get_audio()
            eel.human(text)

            HELP_STRS = ["sure", "yes please", "go ahead"]
            for phrase in HELP_STRS:
                if phrase in text:
                    print("open")
            
eel.start('index.html', size=(480,600), port=8001)



