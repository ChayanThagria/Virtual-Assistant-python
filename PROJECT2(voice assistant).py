import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os

#basic structure
from tkinter import *
root = Tk()
root.geometry("400x140")
root.maxsize(400,140)
root.title("Personal Assistant")
f1 = Frame(root,bg = "black")
f1.pack(fill = BOTH)
output = StringVar()
screen = Entry(f1,textvar = output,bg = "black",fg = "red",font = "Times 18 bold italic")
screen.pack(fill =X)
output.set("")
screen.update()
#basic functions used -
def speak(audio):
    engine = pyttsx3.init('sapi5') #not important
    voice = engine.getProperty('voices') #not important
    engine.setProperty("voice", voice[1].id) #not important
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =  int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        output.set("Good Morning sir")
        screen.update()
        speak("Good Morning Sir")

    elif hour >=12 and hour < 16:
        output.set("Good Afternoon Sir")
        screen.update()
        speak("Good Afternoon Sir")

    elif hour >= 16 and hour < 22:
        output.set("Good Evening Sir")
        screen.update()
        speak("Good Evening Sir")

    else:
        output.set("Good Night Sir")
        screen.update()
        speak("Good Night Sir")

    output.set("How may I help you today?")
    speak("How may I help you today?")
    screen.update()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        output.set("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        screen.update()
    try:
        output.set("Recognising.....")
        query = r.recognize_google(audio, language="en-in")
        output.set(f"user said:{query}\n")
        screen.update()

    except:
        output.set("say again")
        screen.update()
        return None
    return query

x = True
def run_assistant():
    wishme()
    takecommand()
    query = takecommand().lower()
    if "youtube" in query:
        webbrowser.open("youtube.com")

    elif "bye" or "take care" or "fuck off" or "tata" or "close" or "shut down" in query:
        exit()

    elif "google" in query:
        webbrowser.open("google.com")

    elif "instagram" or "insta" in query:
        webbrowser.open("instagram.com")

    elif "facebook" or "fb" in query:
        webbrowser.open("facebook.com")

    elif "shut down sytem" in query:
        os.system("shutdown /s /t 1")

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "who am I" in query:
        speak(r"i'll call you master ")





#button
jarvis_logo = PhotoImage(file = "jarvis_logo_main.png")
jarvis_logo_main = jarvis_logo.subsample(5,5)
B1 = Button(f1,text = "click me",command =run_assistant,image = jarvis_logo_main,bg ="black" )
B1.pack(side = BOTTOM)






root.mainloop()
















