#!/bin/python3.10

# the library for get voices
import os
import pyttsx3
#import webbrowser
#import pyautogui
import time, datetime
import speech_recognition as speech
#from playsound import playsound
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

print("----------------------------YkSy999S----------------------------")

wil = pyttsx3.init()
voices = wil.getProperty("voices")
wil.setProperty("voice",voices[0].id)

def speak(audio):
	wil.say(audio)
	wil.runAndWait()

def getCommands():
	command = speech.Recognizer()
	with speech.Microphone() as mic:
		print("Listen Now....")
		command.phrase_threshold = 0.5
		audio = command.listen(mic)
		try:
			print("Recording....")
			query = command.recognize_google(audio,language="ar-AR")
			print(f'you said : {query}')
		except Exception as error:
			return None
		return query.lower()


while True:
    ring = AudioSegment.from_mp3("./sound/ring.ogg")
    play(ring)

    query = getCommands()

    if query != None:

    	if 'اغلاق' in query:
            print('exit')
            exit()

    	os.system('./tgpt -w "%s" > ./tmp/aitext.txt'%query)
    	bot=os.popen('cat ./tmp/aitext.txt').read()

    	print(bot)

    	obj=gTTS(text=bot,lang='ar',slow=False)
    	obj.save('./tmp/aiaudio.mp3')

    	#playsound('./tmp/aiaudio.mp3')
    	ai = AudioSegment.from_mp3("./tmp/aiaudio.mp3")
    	play(ai)
