import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="put your api Key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client=OpenAI(api_key="put your own api key",
    )
    completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a virtual assistant named Jarvis ,skilled in general tasks like alexa and Google Cloud"},
        {"role":"user","content":command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower.split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=india&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('aarticles',[])

            for article in articles:
                speak(article['title'])
    else:
        #let open ai handle the request
        output=aiProcess(c)
        speak(output)
        



if __name__=="__main__":
    speak("Initializing Jarvis.....")
while True:
    r=sr.Recognizer()
    print("Recognizing.....")
    try:

        with sr.Microphone() as source:
            print("Listening")
            audio=r.listen(source,timeout=2,phrase_time_limit=1)
        command=r.recognize_google(audio)
        if(command.lower()=="jarvis"):
            speak("Ya")
            #Listen for command
            with sr.Microphone() as source:
                print("Jarvis Activating....")
                audio=r.listen(source)
                command=r.recognize_google(audio)

                processCommand(command)

    except Exception as e:
        print("Error;{0}".format(e))
    
        
    