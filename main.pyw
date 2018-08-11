from tkinter import *
from tkinter import messagebox
from threading import Thread
from pygame import mixer
from tkinter import Canvas
import time
from PIL import ImageTk
from PIL import Image


class Timer(Thread):
    over=False
    pause=False
    def __init__(self,func):
        Thread.__init__(self)
        self.func=func
        #self.setDaemon(True)
    def run(self):
        global t,root
        time.sleep(1)
        finish=False
        while not self.over and not finish:
            if not self.pause:
                finish=self.func()
            time.sleep(1)
        if finish:
            #root.focus_force()
            root.event_generate('<<pop>>',when='tail')
            end_time()
        t=None
    def kill(self): self.over=True
    def paus(self): self.pause=True
    def cont(self): self.pause=False

t=None
sec=None
root=Tk()
e1=StringVar()
e2=StringVar()
alarm_name = StringVar()

def show():
    global e1,e2,sec
    e1.set('%.2d'%(sec/60))
    e2.set('%.2d'%(sec%60))
def down():
    global sec
    if sec:
        sec-=1;show()
        return False
    else: return True
def up():
    global sec
    sec+=1;show()
    return False

def reset():
    global sec,t
    if t:t.cont();return
    sec=0;show()
    t=Timer(up)
    t.start()
    mixer.music.stop()

def start():
    global sec,t
    if t:t.cont();return
    sec=0
    try: sec=int(e1.get())*60
    except Exception:pass
    try: sec+=int(e2.get())
    except Exception:pass
    if not sec: return
    show()
    t=Timer(down)
    t.start()

    pass
def pause():
    global t
    t.paus()
    mixer.music.pause()

def volume_up():
    global volumelevel
    mixer.music.set_volume(mixer.music.get_volume() + 0.1)
    volvar.set(mixer.music.get_volume())

def volume_down():
    global volumelevel
    mixer.music.set_volume(mixer.music.get_volume() - 0.1)
    volvar.set(mixer.music.get_volume())

def stop():
    global t,sec
    sec=0;show()
    if t: t.kill()
    t=None
    mixer.music.stop()

def code():
    messagebox.showinfo("Title", "a Tk MessageBox")

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

global volumelevel
mixer.init()
mixer.music.load("analog_alarm.mp3")
volvar = StringVar()
volvar.set(mixer.music.get_volume())


en1 = Entry(root, textvariable = e1,  font = "Calibri 11", bg = "#f7f7f7", justify = CENTER)
en2 = Entry(root, textvariable = e2, font = "Calibri 11",  bg = "#f7f7f7", justify = CENTER)
count1 = Label(root, textvariable = e1, font = "Calibri 25 bold", bg = "#f7f7f7", justify = CENTER)
count2 = Label(root, textvariable = e2, font = "Calibri 25 bold", bg = "#f7f7f7", justify = CENTER)
colon2 = Label(root, text = ":", font = "Calibri 20 bold", bg = "#f7f7f7")
lb = Label(root, text = ':', font = "Calibri 11", bg = "#f7f7f7")
startbtn = Button(root, text='Comienzo', command = start, font = "Calibri 11", bg = "light green")
pausebtn = Button(root, text='Detener', command = pause, font = "Calibri 11", bg = "#ff887f")
stopbtn = Button(root, text='Reiniciar', command = stop, font = "Calibri 11", bg = "light blue")
codebtn = Button(root, text='Código', command = code, font = "Calibri 11")
watchbtn = Button(root, text='Watch', command = set_analog, font = "Calibri 11")
purgebtn = Button(root, text='Purge', command = set_purge, font = "Calibri 11")
tornadobtn = Button(root, text='Tornado', command = set_tornado, font = "Calibri 11")
gameoverbtn = Button(root, text='Game Over', command = set_game_over, font = "Calibri 11")


count1.grid(row = 2, column = 0, rowspan = 2, columnspan = 2)
count2.grid(row = 2, column = 3, rowspan = 2, columnspan = 2)
colon2.grid(row = 2, column = 2, rowspan = 2)
en1.grid(row = 1, column = 0, columnspan = 2, padx = 15)
en1.columnconfigure(1, minsize=1, weight = 0)
lb .grid(row = 1, column = 2, padx= 4, pady = 4)
en2.grid(row = 1, column = 3, columnspan = 2, padx = 15)
en2.columnconfigure(1, minsize=1, weight = 0)
pausebtn.grid(row = 0, column = 5, padx= 4, pady = 4)
startbtn.grid(row = 1, column = 5, )
stopbtn.grid(row = 2, column = 5, padx= 4, pady = 4)
codebtn.grid(row = 3, column = 5, padx= 4, pady = 4)
watchbtn.grid(row = 0, column = 0, padx= 4, pady = 4)
purgebtn.grid(row = 0, column = 1, padx= 4, pady = 4)
tornadobtn.grid(row = 0, column = 2, padx= 4, pady = 4)
gameoverbtn.grid(row = 0, column = 3, padx= 4, pady = 4)
root.geometry('+400+500')
root.config(bg = "#f7f7f7")
root.title("Komocki Timer")
root.mainloop ()
