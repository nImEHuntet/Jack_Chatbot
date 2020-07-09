#jack_chatbot(0.0.1) initial commit
#jack_chatbot(0.0.2) code cleanup and optimization
#
##
### written by AYUSHMAAN KARMOKAR (nimehuntetd)
##
#
# modules import
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter.messagebox

from dependencies.random import choice
import time, datetime, webbrowser

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

# for messagebox defination function
# need more documentation
def about_us():
    tkinter.messagebox.showinfo('about me','''Chabot jack 0.0.1 - Python3.8.0 By(ayushmaan_karmokar)
PLEASE DO NOT USE PUNCTUATIONS AS THEY ARE NOT SUPPORTED YET !!''')

def how_to_use():
    tkinter.messagebox.showinfo('info!','''1. hello   = ["hi", "hello","whatsup","moshi moshi","hai"]
2. weather = ["whats the weather today","weather","i feel cold","tenki dane","will it rain"]
3. version = ["info","version","will you get updated"]\n4. help1 = ["help"]''')

def click_on_image():
    webbrowser.open_new_tab('documentation.html')
    
# inputs from users                                   
hello   = {"hi", "hello","whatsup","moshi moshi","hai"}
weather = ["whats the weather today","weather","i feel cold","tenki dane","will it rain"]
version = ["info","version","will you get updated"]
help1 = ["help"]
doc = ["open documentation","documentation"]

# outputs from jack
hello_out    = ["Hi, I'm jack", "Hello, it's jack.", "Hello to you too"]
weather_out = ["hmm, the temperature in your area is 26 degree C","im not ready yet to know about weather"]
version_out = ["jack at 0.0.1 running on python","0.0.1"]
help1_out = ["see console"]
error = ["I do not know what you mean by that, enter help to know more about me.", "uhm, what does that mean.",
         "I'm sorry, can you repeat again?","enter help to see what i can do"]            

# window and string var (GUI)                                                                  
root = tk.ThemedTk()
root.get_themes()           
root.set_theme("black")                            
user = StringVar()                          
bot  = StringVar()

# cosmetics                                   
root.title("jack-Chatbot (0.0.1)(0.0.2)-increment")
statusbar = ttk.Label(root, text="Welcome to Chatbot with jack: Status NORMAL", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)

menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=Tk.destroy)
subMenu.add_command(label="More Options Soon!")

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)
subMenu.add_command(label="How to Use?", command=how_to_use)

src = PhotoImage(file='src/logo.png')
src1 = ttk.Button(root, image=src, command=click_on_image)
src1.pack(side=LEFT)
Label(root, text=" user : ",fg="green").pack(side=LEFT)                
Entry(root, textvariable=user).pack(side=LEFT,ipadx=20)          
Label(root, text=" Bot  : ",fg="blue").pack(side=LEFT)                
Entry(root, textvariable=bot).pack(side=LEFT,ipadx=20)

# main code jack execution                                
def main():
    statusbar.config(text="Welcome to Chatbot with jack: Status NORMAL")
    file1=open("bash.jack","a")
    datatime=str(datetime.datetime.now()) #run date $ time
    file1.write("\n new data collection: ")
    file1.write(datatime)
    file1.write("***********************\n\n")
    file2=open("error.jack","a")
    question = user.get()
    if question in hello:
        output=choice(hello_out)
        bot.set(output)
        speak.Speak(output) 
        
    elif question in weather:
        output=choice(weather_out)
        bot.set(output)
        speak.Speak(output)
        
    elif question in version:
        output=choice(version_out)
        bot.set(output)
        speak.Speak(output)
        
    elif question in help1:
        output=choice(help1_out)
        print(" to say hi: ",hello,"\n","weatherinfo: ",weather,"\n","version: ",version)
        bot.set(output)
        speak.Speak(output)
        
    elif question in doc:
        output("See documentation, opening browser")
        bot.set(output)
        speak.Speak(output) 
        webbrowser.open_new_tab('documentation.html')
        
    else:
        datatime_error=str(datetime.datetime.now())
        file2.write("\ndatetime: ")
        file2.write(datatime_error)
        file2.write("error below: ")
        output=choice(error)
        statusbar.config(text="Welcome to Chatbot with jack: Status UNKNOWN")
        bot.set(output)
        speak.Speak(output)
    file1.write("\n")
    file1.write("user: ")
    file1.write(question)
    file1.write("\njack: ")
    file1.write(output)
    file1.close()
    file2.close()
    
                                
Button(root, text="| C H A T |",fg="red", command=main).pack(side=LEFT)

mainloop()
#code_end
