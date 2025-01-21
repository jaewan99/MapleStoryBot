from pyautogui import *
# import pyautogui
import pydirectinput

import time
import keyboard
import random
import win32api, win32con
import cv2
pydirectinput.PAUSE = 0.00


import threading

import os
import sys



from tkinter import *

lay=[]
root = Tk()
root.geometry('300x400+100+50')

def create():

    top = Toplevel()
    lay.append(top)

    top.title("Main Panel")
    top.geometry('500x500+100+450')
    msg = Message(top, text="Show on Sub-panel",width=100)
    msg.pack()

    def exit_btn():

        top.destroy()
        top.update()

    btn = Button(top,text='EXIT',command=exit_btn)
    btn.pack()


Button(root, text="Click me,Create a sub-panel", command=create).pack()
mainloop()