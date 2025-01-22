from pyautogui import *
import pyautogui
import pydirectinput

import time
import keyboard
import random
import win32api, win32con
import cv2
pydirectinput.PAUSE = 0.00

attack6 = cv2.imread(r"C:\Users\Administrator\Desktop\john\autogui\testing\attack6.png") 
attack3 = cv2.imread(r"C:\Users\Administrator\Desktop\john\autogui\testing\attack3.png") 
attack1 = cv2.imread(r"C:\Users\Administrator\Desktop\john\autogui\testing\attack1.png")
attack2 = cv2.imread(r"C:\Users\Administrator\Desktop\john\autogui\testing\attack2.png")
cubeChecker = cv2.imread(r"C:\Users\Administrator\Desktop\john\autogui\testing\cubeChecker.png")
# pyautogui.locateOnScreen(attack6, region=(310,360, 180, 80)) x=380, y=450


# testing

# pic = pyautogui.screenshot(region=(310,360, 180, 80))
# pic.save(r"C:\Users\Administrator\Desktop\john\autogui\testing\큐브.png")


# 600 start
sleep(1)

def retry():
    pyautogui.click(380,450)
    sleep(.1)
    pydirectinput.press('enter')
    sleep(.1)
    pydirectinput.press('enter')
    sleep(.1)
    pydirectinput.press('enter')
    sleep(.1)


def cubeCheck():
    if pyautogui.locateOnScreen(cubeChecker, region=(310,360, 180, 80), confidence = .98) == None:
        time.sleep(.1)
        pydirectinput.press('tab')
        time.sleep(.1)
        pydirectinput.doubleClick(630,315)
        time.sleep(.1)
        pydirectinput.click(630,315)
        time.sleep(.1)
        pydirectinput.press('enter')





while keyboard.is_pressed('s') == False:




    if pyautogui.locateOnScreen(attack6, region=(310,360, 180, 80)) != None or pyautogui.locateOnScreen(attack2, region=(310,360, 180, 80)) != None:
        print('found1')
        twelvePercent = list(pyautogui.locateAllOnScreen(attack2, confidence= 0.98, region=(310,360, 180, 80)))
        if pyautogui.locateOnScreen(attack3, region=(310,360, 180, 80),confidence=0.98) != None or pyautogui.locateOnScreen(attack1, region=(310,360, 180, 80)) != None:
            print('found2')
            break
        elif (len(twelvePercent)) == 2:
            print('found2')



            break
        retry()
    else:
        cubeCheck()
        retry()
        
    sleep(.7)










