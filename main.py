import sys
import speech_recognition as sr
import subprocess as sp
from gtts import gTTS
from pygame import mixer
from playsound import playsound
from gcp import *
import os
import time
import random

def talkToMe(audio):
    r1 = random.randint(1,1000000000)
    r2 = random.randint(1,10000000000)
    randfile = str(r2) + "randomtext" + str(r1) + ".mp3"
    tts = gTTS(text=audio, lang='en')
    tts.save(randfile)
    playsound(randfile)
    print(audio)
    

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print('You said: ' + command + '\n')
            return command
        except sr.UnknownValueError:
            assistant(myCommand())

    

def assistant(command):
    if 'what is my organisation name' in command:
        org_name = getOrgName()
        talkToMe(org_name)
        #removeAudio()
    elif 'what is my organisation ID' in command:
        org_id = getOrgId()
        talkToMe('Here is your organisation identification number')
        print(org_id)
        #removeAudio()
    elif 'how many instances do I have' in command:
        instance_list = ListInstances()
        #print('You have %s instances' %(str(len(instance_list))))
        for instance in instance_list:
            speak = "Here is the list of your Instances"
            talkToMe(speak)
            print(instance)
    elif 'how many vms do I have' in command:
        instance_list = ListInstances()
        #print('You have %s instances' %(str(len(instance_list))))
        for instance in instance_list:
            speak = "Here is the list of your Instances"
            talkToMe(speak)
            print(instance)
    elif 'stop' in command:
        bye = "Okay, Bye Bye"
        talkToMe(bye)
        try:
            removeAudio()
        except Exception as e:
            pass
        sys.exit()
        
    else:
        print('Sorry, I have not learned that yet.')
        sorry = "Sorry, I have not learned that yet."
        talkToMe(sorry)
        

def removeAudio():
    files = os.listdir()
    for file in files:
        if file.endswith('.mp3'):
            os.remove(file)    


while True:
    command = myCommand()
    assistant(command)





