# Voice-command-system-for-visually-impaired-person-demo-model
This is a project to make an interactive voice recognition and command system for visually impaired persons. 

Here the system is built on top of the Google speech recognition module. 

The main build is the file utils_sensation.py which is inherited by the file main_sensation.py

The program when executed (execute the main_sensation.py) asks to select a language between 2 options "English" and "German". If we take too long to choose the instruction language then it will automatically choose English as its default language. After one of the languages is selected we will get 3 options "start", "time", and "stop". We have the provision to add many more features/options to the code but as a demo code, I have added only 3 options. If start is selected it will start the attached navigation device, if time is selected it will tell the current time and if stop is selected it will stop the navigation device and terminate the command and execution of the code.
Apart from all these above options the code has the provision to change the instruction language from English to german or German to english by verbally passing the command "change language".

The code keeps on running continuously and keeps on listening to your commands unless and until a verbal "stop" command is passed. 

Note: Google speech recognition module sometimes does not recognize your voice command or sometimes it takes a long to register your command so you have to be a bit patient to get the desired result in the end.
If you want you can replace the Google speech recognition module with more latest Morzilla Deep Speech module for better performance. 
