import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import playsound
from gtts import gTTS
import random
r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            jarvis_speak (ask)
        audio=r.listen(source)
        voice_data=""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            jarvis_speak("sorry i did not catch what you said")
        except sr.RequestError:
            jarvis_speak("sorry my speech service is down")

        return voice_data        

def jarvis_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,1000000)
    audio_file='audio-'+str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "what is your name" in voice_data:
        jarvis_speak("I'm jarvis")
    if "what time is it" in voice_data:
        jarvis_speak(ctime())    
    if "search" in voice_data:
        search=record_audio('what do you want to search for ?')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        jarvis_speak("here is what i found for "+search)
    if "location" in voice_data:
        location=record_audio("what location would you like to find")
        url="https://google.ml/maps/place/"+location+"/&amp"
        webbrowser.get().open(url)
        jarvis_speak("here is what i found about "+location)
    if "exit" in voice_data:
        exit()
time.sleep(1)


jarvis_speak("how can i help you")
while 1:
    voice_data=record_audio()
    respond(voice_data)

