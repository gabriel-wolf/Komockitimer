#!/usr/bin/env python
from tkinter import *
import time
import sys
from pygame import mixer
root = Tk()
TimerFont0="'Helvetica', 20"
TimerFont1="'Helvetica', 15"
global msecs, time1, time2, q
time1 = ''
time2 = ''
q=0
msecs=0
alarm_name = StringVar()

ButtonFont1="'Helvetica', 10"
clock = Label(root, text="Komocki Timer", font=TimerFont1)
clock.grid( row=0, column=0,columnspan=6)

def set_analog():
    global alarm_choose
    alarm_choose = "analog_alarm.mp3"
    watchbtn.config(fg = "blue")
    purgebtn.config(fg = "black")
    tornadobtn.config(fg = "black")
    gameoverbtn.config(fg = "black")

def set_purge():
    global alarm_choose
    alarm_choose = "purge_siren.mp3"
    purgebtn.config(fg = "blue")
    watchbtn.config(fg = "black")
    tornadobtn.config(fg = "black")
    gameoverbtn.config(fg = "black")

def set_tornado():
    global alarm_choose
    alarm_choose = "tornado_siren.mp3"
    tornadobtn.config(fg = "blue")
    purgebtn.config(fg = "black")
    watchbtn.config(fg = "black")
    gameoverbtn.config(fg = "black")

def set_game_over():
    global alarm_choose
    alarm_choose = "game_over.mp3"
    gameoverbtn.config(fg = "blue")
    tornadobtn.config(fg = "black")
    purgebtn.config(fg = "black")
    watchbtn.config(fg = "black")

def end_time():
    global alarm_name
    mixer.init()
    mixer.music.load("" + alarm_choose)
    print(alarm_choose)
    mixer.music.play()

def tick(msecs):
    clock.config(font=TimerFont1)
    time1 = int(time.time())
    msecs=int(msecs)*60 +1
    q=msecs

    while (msecs >=0):
        if msecs> 60:
            clock.config(fg='black')
        msecs -=1
        mi = int(msecs/60)
        m = str(mi)
        if mi <10:
            m = '0'  + str(mi)
        se = msecs - (mi*60)
        s = str(se)
        if se <10:
            s = '0' +str(se)
        clock.config(text= m + ':' + s)
        if msecs < 60:
            clock.config(fg='orange')
        if msecs < 30:
            clock.config(fg='red')
        root.update()
        time2 = int(time.time())
        while time2 == time1:
            time2 = int(time.time())
        time1=time2
        print(msecs)
    global alarm_name
    mixer.init()
    mixer.music.load("" + alarm_choose)
    print(alarm_choose)
    mixer.music.play()
    clock.config(text=" TIME ", font=TimerFont1)
    clock.update_idletasks()


def disp():
    msecs=-1
    print(msecs)
    clock.config(text=" TIME ", font=TimerFont1)
    clock.update_idletasks()

mixer.init()
mixer.music.load("analog_alarm.mp3")

watchbtn=Button(text='Watch', width=8, font=ButtonFont1, command=set_analog)
watchbtn.grid(row=1, column=0)
purgebtn=Button(text='Purge', width=8, font=ButtonFont1, command=set_purge)
purgebtn.grid(row=1, column=1)
tornadobtn=Button(text='Tornado', width=8, font=ButtonFont1, command=set_tornado)
tornadobtn.grid(row=1, column=2)
gameoverbtn=Button(text='Game Over', width=8, font=ButtonFont1, command=set_game_over)
gameoverbtn.grid(row=1, column=3)
buttonB4=Button(text='4 minutes', width=8, font=ButtonFont1, command=lambda:tick(0.02))
buttonB4.grid(row=1, column=4)
buttonB5=Button(text='2 minutes', width=8, font=ButtonFont1, command=lambda:tick(2))
buttonB5.grid(row=1, column=5)

label1=Label(root,text="Español es muy bueno!", font=ButtonFont1)
label1.grid(row=2, column=2,columnspan=2)
button6 = Button(root, text='Start Timer', font=ButtonFont1, command=lambda:tick(int(entry1.get())))
button6.grid(row = 4, column = 2,columnspan=2)
entry1=Entry(root, font=ButtonFont1)
entry1.grid(row=3, column=2,columnspan=2)
button7 = Button(root, text='Stop Timer', font=ButtonFont1, command=disp)
button7.grid(row = 5, column = 2,columnspan=2)

root.geometry('440x180+200+5')
root.mainloop(  )
