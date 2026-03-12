import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Could not understand audio")

def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 1.0)

if __name__ == '__main__':
    if "peter" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "hi hello" in data1:
                greet = "hello! nice to meet you!"
                speechtxt(greet)
            if "how are you" in data1:
                greet1 = "I am fine, thank you!"
                speechtxt(greet1)
            if "your name" in data1:
                name = "my name is friday"
                speechtxt(name)
            elif "old are you" in data1:
                age = "I am new"
                speechtxt(age)
            elif 'now time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtxt(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'spotify' in data1:
                webbrowser.open("https://www.spotify.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                speechtxt(joke_1)
            elif "chatGPT" in data1:
                webbrowser.open("https://chatgpt.com/")
            # elif 'play song' in data1:
            #     add = "C:\sukhendu\songs"
            #     listensong = os.listdis(add)
            #     print(listensong)
            #     os.startfile(os.path.join(add, listensong[0]))
            elif "exit" in data1:
                speechtxt("Thank you for playing")
                break
            # time.sleep(8)
    else:
        print("Thanks for playing")
