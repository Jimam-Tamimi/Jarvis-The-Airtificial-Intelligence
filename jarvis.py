import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from random import randint

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice)
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 150)

# Making the speak function so that our Jarvis can speak 
def speak(text, pr=1):
    if pr==1:
        print(text)
    engine.say(text)
    engine.runAndWait()
# speak('Hello World')


def wish():
    date = datetime.datetime.now().hour
    # print(date)
    if date<12:
        speak('Good Morning sir.')
    elif date<18:
        speak('Good Afternoon sir.')
    elif date<24:
        speak('Good Evening sir.')
    speak("I am Jarvis. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        print(f'User said : {query}')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query

if __name__ == "__main__":   
    wish()
    
    # Wring the logic of the program
    while True:
        query = takeCommand().lower()

        if query == 'search':
            speak('Yes sir.\nI am listing.\nTell me how may I help you...')
            while True:
                query = takeCommand().lower()
                if 'tell me' in query or 'wikipedia' in query:
                    speak('Searching in wikipedia...')
                    query = query.replace('tell me', '')
                    try:
                        results = wikipedia.summary(query, sentences=5)
                        speak(f'\nAccroding to wikipedia, {results}')
                    except Exception as e:
                        speak("Sorry, couldn't find any result..")

                elif 'search in google' in query or  'google search' in query or 'search google' in query or 'google search' in query  :
                    speak('What should I search for you...')
                    googleSearchQuery = takeCommand().lower()
                    speak('Searching in google about this topic...')
                    webbrowser.open(f"https://www.google.com/search?q={googleSearchQuery}")
                        
                elif 'open google' in query or 'go to google' in query:
                    speak('Opening Google')
                    webbrowser.open('https://google.com/')

                elif 'open facebook' in query or 'go to facebook' in query:
                    speak('Opening Facebook')
                    webbrowser.open('https://facebook.com/')

                elif 'open stack overflow' in query or 'go to stack overflow' in query:
                    speak('Opening Stackoverflow')
                    webbrowser.open('https://stackoverflow.com/')
                elif 'open git hub' in query or 'go to git hub' in query or 'git hub' in query:
                    speak('Opening Github')
                    webbrowser.open('https://github.com/')

                elif 'open youtube' in query or 'go to youtube' in query:
                    speak('Opening Youtube')
                    webbrowser.open('https://youtube.com/')

                elif 'open code with harry' in query or 'go to code with harry' in query or 'code with harry' in query:
                    speak('Opening Your Favourate Channel')
                    webbrowser.open('https://youtube.com/')

                elif 'open messenger' in query or 'go to messenger' in query:
                    speak('Opening Messenger')
                    webbrowser.open('https://www.facebook.com/messages/')

                elif "open fn's club" in query or "go to fn's club" in query or "fn's club" in query or "club" in query:
                    speak("Opening Fn'sclub") 
                    webbrowser.open('https://club.fnsoftwares.com/')

                elif 'open google activity' in query or 'google activity' in query or 'open my activity' in query or 'my activity.google' in query or 'my activity.google.com' in query or 'my activity' in query or 'check my google activity' in query :
                    speak('Opening Your ') 
                    webbrowser.open('https://myactivity.google.com/')

                elif "ok go now" in query or  "go" in query or  "go now" in query or "ok stop now" in query or "ok stop" in query or "stop" in query or  "you can stop" in query or "stop now" in query:
                    speak('Thank you sir.\nCall me anytime.')
                    query.replace(query, '')
                    break
                
                else:
                    n = randint(1, 5)
                    if n == 1:
                        speak("Sir, should I stop?")
                    elif n == 2:
                        speak("Sir, what should I do now?")
                    elif n == 2:
                        speak("Sir, should I do anything more?")
                    elif n == 3:
                        speak("What else I have to do sir?")
                    elif n == 4:
                        speak("Anything else sir?")
                    elif n == 5:
                        speak("Please give me an order sir")
                    elif n == 6:
                        speak("Sir, Should I go now?")
        elif 'exit' in query or 'done' in query:
            exit()




# https://www.google.com/search?q=myactivity