import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import pywhatkit as kit
import requests
import smtplib
import shutil
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    assname = ("Jarvis")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should I call you?")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Hello", uname.center(columns))
    print("#####################".center(columns))

    speak("How can I Help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    assname = ("Jarvis")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should I call you?")
    uname = takeCommand()
    speak("Hello")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Hello", uname.center(columns))
    print("#####################".center(columns))

    speak("How can I help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'who is' in query:
            speak('Searching The Internet...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to the Internet")
            print(results)
            speak(results)

        # Website Search
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Over flow. Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open spotify web' in query:
            speak("Opening Spotify\n")
            webbrowser.open("open.spotify.com")

        # Open any application
        elif 'open discord' in query:
            appli = r"C:\Users\User\AppData\Local\Discord\app-1.0.9005\Discord.exe"
            os.startfile(appli)

        # Functions
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        elif "calculate" in query:

            app_id = "AppId"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        # Exit the program
        elif 'stop listening' in query:
            speak("Thanks for giving me your time")
            exit()

