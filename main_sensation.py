#!/usr/bin/env python
# coding: utf-8

# In[4]:


import speech_recognition as sr
import pyaudio
import pyttsx3
from datetime import datetime
import time
from utils_sensation import sensation
#!pip install pyttsx3


# In[2]:


obj = sensation()
var = obj.recognition()
obj.languages(var)
#while True:
if var != 'english' and var!= 'german' and var != 'stop':
        #obj.engine.say('please choose, between debu, english and german')
        #obj.engine.runAndWait()
    var = obj.recognition()
    obj.languages(var)
    #else:
     #   break


# In[ ]:




