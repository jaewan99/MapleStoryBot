from pyautogui import *
import pyautogui
import pydirectinput

import time
import keyboard
import random
import win32api, win32con
import cv2
pydirectinput.PAUSE = 0.00




sleep(1)


while keyboard.is_pressed('r') == False:
    if keyboard.is_pressed('f'):
        print('rest')
        sleep(8)
        print('go')
        sleep(1)

    pyautogui.click()
    sleep(.1)