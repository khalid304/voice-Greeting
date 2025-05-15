import pyttsx3
import datetime


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour=datetime.datetime.now().hour
    if 0 <= hour <12:
        speak('good morning khalid')
    elif 12 <= hour <16:
        speak("good afternoon khalid")
    elif 16 <= hour <21:
        speak("good evening khalid")    
    else:
        speak("good ninght khalid")

if __name__ == "__main__":
    greet_user()

