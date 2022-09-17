import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('QAEXLK-RY9HY2PHAT')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    elif currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')
    speak("I am Jarvis sir. Please tell me how may I help you")

greetMe()

speak('Hello Gopal, I am your personal assistant!')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print('Sorry Gopal! I didn\'t get that! Try typing the command!')
        # query = str(input('Command: '))
        return "None"
    
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("gopalmgk1997@gmail.com", "password")
    server.sendmail('gopalmgk1997@gmail.com',to, content)
    server.close()
        
    


if __name__ == '__main__':

    while True:

        query = myCommand().lower()
        # query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'play music' in query:
            music_folder = "C:\\Users\\Admin\\Desktop\\Music"
            songs =os.listdir(music_folder)
            # random_music = music_folder + random.choice("Music") + '.mp3'
            # os.system(random_music)
            print(songs)
            os.startfile(os.path.join(music_folder, songs[0]))

            speak('Okay, here is your music! Enjoy!')

    
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentances = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)




        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('ok')
            speak('Bye Gopal, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Gopal')

        elif 'bye' in query:
            speak('Bye Gopal, have a good day.')
            sys.exit()

        



        elif 'email to ayush' in query:
            try:
                speak('What should I say? ')
                content = myCommand()
                to = "gupgaayush@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak('Sorry Gopal! I am unable to send your message at this moment!')

        speak('Next Command! Gopal!')
