import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess as sp
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # type: ignore
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")

    elif hour >= 16 and hour >= 20:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I am jarvis, mam. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # type: ignore
        print(f": Your Command : {query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "_main_":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackover flow' in query:
            webbrowser.open("stack over flow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")

        elif ' open code ' in query:
            codePath = "C:\\Users\\DELL\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        def open_camera():
            sp.run('start microsoft.windows.camera:', shell=True)

        def open_cmd():
            os.system('start cmd')

       # def find_my_ip():
           # ip_address = requests.get(
               # 'https://api64.ipify.org?format=json').json()
            #return ip_address["2401:4900:1c62:e14:4d19:4359:756b:c988"]

       # def play_on_youtube(video):
      #     kit.playonyt(video)

        def get_random_advice():
            res = requests.get("https://api.advice slip.com/advice").json()
            return res['slip']['advice']
