#!/usr/bin/env python
# coding: utf-8

# In[2]:


import speech_recognition as sr
import pyaudio
import pyttsx3
from datetime import datetime
import time
from demo import demo


# In[3]:


class sensation():
    def __init__(self):
        self.engine = pyttsx3.init()
        #self.engine2 = pyttsx3.init()
        self.engine.setProperty('voice', 'english')# Set the voice (you can change 'en' to a different language code)
        #self.engine2.setProperty('voice', 'german')
        self.engine.setProperty('rate', 150)# Set the speech rate (words per minute)
        #self.engine2.setProperty('rate', 150)
        self.text = "welcome to sensation, please select the instruction language between english and german"
        self.engine.say(self.text)
        self.engine.runAndWait()
        self.a = sr.Recognizer()
        self.count = 0
        self.flag = False
        self.unknow = False
        
    def recognition(self):
    
        try:
            with sr.Microphone() as source:
                self.a.adjust_for_ambient_noise(source)
                audio = self.a.listen(source)
                text = self.a.recognize_google(audio)
                text = text.lower()
                self.unknown = False
                print(text)
                return text
            
        except sr.UnknownValueError:
            #print('unknown debu')
            self.count = self.count+1
            self.unknown = True
            if self.count == 1 and self.unknown == True:
                self.count = 0
                self.unknown = False
                self.engine.setProperty('voice', 'english')
                self.engine.say('default language english has been selected')
                self.engine.runAndWait()
                return str('english')
            
            elif self.count == 3:
                self.count = 0
                self.engine.setProperty('voice', 'english')
                self.engine.say('please choose between start, stop and time, I am waiting')
                self.engine.runAndWait()
            
            elif self.count == 4:
                self.count = 0
                self.engine.setProperty('voice', 'german')
                self.engine.say('Bitte wählen Sie zwischen Start, Stopp und Zeit, ich warte')
                self.engine.runAndWait()
                
            else:
                #print('test pass', self.count, self.unknown)
                pass
#var = recognition()
    def en_input(self,var):
        var = var
        if var == 'start':
            #debu_obj = demo()  ## replace this file with useful files
            self.engine.say('navigation started')
            self.engine.runAndWait()
            
        elif var == 'stop':
            self.engine.say('navigation stopped')
            self.engine.runAndWait()
            self.engine.stop()
            #break
            #ass
            
        elif var == 'time':
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M")
            currentTime = currentTime.split(':')
            self.engine.say('the current time is {} hours and {} minutes'.format(currentTime[0],currentTime[1]))
            self.engine.runAndWait()
            
        else:
            self.engine.say('please choose between start, stop and time')
            self.engine.runAndWait()
            
            
            
    def de_input(self,var):
        var = var
        if var == 'start':
            #debu_obj = demo()  ##replace this file with useful files
            self.engine.say('Navigation gestartet')
            self.engine.runAndWait()
            
        elif var == 'stopp'or var == 'stop':
            self.engine.say('Navigation gestoppt')
            self.engine.runAndWait()
            self.engine.stop()
            #break
            #ass
            
        elif var == 'zeit':
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M")
            currentTime = currentTime.split(':')
            self.engine.say('Die aktuelle Zeit beträgt {} Stunden und {} Minuten'.format(currentTime[0],currentTime[1]))
            self.engine.runAndWait()
            
        else:
            self.engine.say('Bitte wählen Sie zwischen Start, Stopp und Uhrzeit')
            self.engine.runAndWait()
            
            

    def languages(self,var):
        var = var
        
    
        if var == 'english':
            # = True
            self.engine.setProperty('voice', 'english')
            self.engine.say('english has been selected as the instruction language')
            self.engine.runAndWait()
            while True:
                #self.count = 0
                self.count = self.count + 2
                var = self.recognition()
                if self.unknown == False:
                    var = var.lower()
                    if var != 'change language':
                        self.en_input(var)
                    
                        if var == 'stop' or var == 'stopp':
                            #elf.flag = True
                            print('debu')
                            break
                        
                        else:
                            continue
                    #reak
                
                
                
                    else:
                        self.flag= True
                        self.engine.say('please choose between english and german')
                        self.engine.runAndWait()
                    
                        break
                    
                else:
                    print('test continue')
                    continue
                
            
            if self.flag == True:
                self.flag = False
                var = self.recognition()
                
                self.languages(var)
                
            
        
        #engine.stop()
        #engine.runAndWait()
        
            
        elif var == 'german':
            self.engine.setProperty('voice', 'german')
            #self.engine.say('german has been selected as the instruction language')
            self.engine.say('Als Unterrichtssprache wurde Deutsch gewählt')
            self.engine.runAndWait()
            while True:
                #self.count = 0
                self.count = self.count + 3
                var = self.recognition()
                if self.unknown == False:
                    var = var.lower()
                    if var != 'change language' and var != 'sprache andern':
                        self.de_input(var)
                    
                        if var == 'stopp' or var == 'stop':
                            #elf.flag = True
                            print('debu')
                            break
                        
                        else:
                            
                            continue
                    
                
                
                
                    else:
                        self.flag= True
                        self.engine.say('Bitte wählen Sie zwischen Englisch und Deutsch')
                        self.engine.runAndWait()
                    
                        break
                        
                else:
                    continue
                
            
            if self.flag == True:
                self.flag = False
                var = self.recognition()
                
                self.languages(var)
        #engine.stop()
        #ngine.runAndWait()
        
            
        else:
            if var != 'stop' and var!='stopp':
                self.engine.setProperty('voice', 'english')
                self.engine.say('Unrecognized language, please choose between english and german')
                self.engine.runAndWait()
                var = self.recognition()
                self.languages(var)
                #self.flag = False
            else:
                self.engine.setProperty('voice', 'english')
                self.engine.say('Navigation stopped')
                self.engine.setProperty('voice', 'german')
                self.engine.say('Navigation gestoppt')
                
                self.engine.runAndWait()
                self.engine.stop()
                #pass
        #ngine.stop()
        
        #recognition()
    #recognition()


# In[ ]:




