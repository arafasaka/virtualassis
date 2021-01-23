import os
import subprocess

filename = "english assignment.docx"
result = []
for root, dir, files in os.walk("C:\\Users"):
   if filename in files:
      result.append(os.path.join(root, filename))
      os.startfile(os.path.join(root, filename))

print(result)


def files(text):
    eel.computer("Sure, is it word, excel, or power point?")
    speak("Sure, is it word, excel, or power point?")
    files_term = get_audio()
    eel.human(files_term)
    eel.computer("could you please tell me the name of the file?")
    speak("could you please tell me the name of the file?")
    filename_term = get_audio()
    eel.human(filename_term)
    if files_term == "maybe":
        word(filename_term)
    elif files_term == "excel document" or "excel":
        excel(filename_term)
    elif files_term == "power point document" or "powerpoint":
        ppt(filename_term)
    else:
        eel.computer("I'm, sorry i didn't get that")
        speak("I'm, sorry i didn't get that")
        
def word(filename_term):
    filename = "english assignment" + ".docx"
    result = []
    for root, dir, files in os.walk("C:\\Users"):
        if filename in files:
            result.append(os.path.join(root, filename))
            os.startfile(os.path.join(root, filename))
        else:
            speak("fuck")
            return

    print(result)
    eel.computer(result)
    print(filename)

def excel(text):
    filename = text + ".xlsx"
    result = []
    for root, dir, files in os.walk("C:\\Users"):
        if filename in files:
            result.append(os.path.join(root, filename))
            os.startfile(os.path.join(root, filename))
        else:
            eel.computer("Sorry i can't find it")
            print("Sorry i can't find it")
            speak("Sorry i can't find it")
            return
    print(result)
    eel.computer(result)
    print(filename)

def ppt(text):
    filename = text + ".pptx"
    result = []
    for root, dir, files in os.walk("C:\\Users"):
        if filename in files:
            result.append(os.path.join(root, filename))
            os.startfile(os.path.join(root, filename))
        else:
            eel.computer("Sorry i can't find it")
            print("Sorry i can't find it")
            speak("Sorry i can't find it")
            return

    print(result)
    eel.computer(result)
    print(filename)