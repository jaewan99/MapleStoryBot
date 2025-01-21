
import pydirectinput
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2


from tkinter import *
#from tkinter.ttk import Frame, Button, Entry, Style


from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import messagebox
from python_imagesearch.imagesearch import imagesearcharea

pydirectinput.PAUSE = 0.00

#for multithreding 
import threading


violetta = cv2.imread(r"C:\Users\Administrator\Desktop\john\autogui\testing\violetta.png") 

#for multiprocessing
#import multiprocessing
#from multiprocessing import Process

import os
import sys

"""
def moving():
    while myXPosition != runeXPosition:
        if myXPosition < runeXPosition:
            pydirectinput.keyUp('right')
        elif myXPosition > runeXPosition:
            pydirectinput.keyUp('left')

    pydirectinput.press('right')
    pydirectinput.press('left')
"""

 
def testing():
    
    time.sleep(1)
    right = 0
    left = 0
    runeFound = 0

    pic = pyautogui.screenshot(region=(10,90,170,60))
    #pic.save(r"C:\Users\Administrator\Desktop\새 폴더\autogui\testing\runes.png")
    width, height = pic.size
    # try for loop in whole screen
    
    for x in range (0, width, 2):
        for y in range (0, height, 2):
            r,g,b = pic.getpixel((x,y))
            if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                
                # this line is only for 길쪽 동글숲
                if (x != 98) and (y != 44):
  
                   
                    myXPosition = x
                    #print(x + 10 )
                    myYPosition = y
                    
                    #print (y+90)
                
            
                
            if (r == 221) and (g == 102) and (b == 255):
                runeFound = 1
                runeXPosition = x
                runeYPosition = y
                
                

    
    if runeFound == 0:
        print('none')
    if runeFound != 0:
        runeXRightPosition = runeXPosition+5
        runeXLeftPosition = runeXPosition-5
        while myXPosition > runeXRightPosition or runeXLeftPosition > myXPosition:
            if myXPosition < runeXPosition:
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('right')
                 
                
                right = 1

            elif myXPosition > runeXPosition:
                pydirectinput.keyUp('right')
                pydirectinput.keyDown('left')
                 
                left = 1

            pic = pyautogui.screenshot(region=(10,90,350,200))
            width, height = pic.size
            for x in range (0, width, 2):
                for y in range (0, height, 2):
                    r,g,b = pic.getpixel((x,y))
                    if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                        if (x != 98) and (y != 44):
                            
                            myXPosition = x
                            myYPosition = y
            

        if right == 1:
            pydirectinput.keyUp('right')
            pydirectinput.keyUp('left')
            pydirectinput.press('left')

        elif left == 1:
            pydirectinput.keyUp('left')
            pydirectinput.keyUp('right')
            pydirectinput.press('right')


        runeYUpPosition = runeYPosition+4
        runeYDownPosition = runeYPosition-4
        while myYPosition > runeYUpPosition or   runeYDownPosition> myYPosition:
            if myYPosition < runeYPosition:
                pydirectinput.keyDown('down')
                time.sleep(.1)
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.keyUp('down')
                time.sleep(2)
            else:
                pydirectinput.press('r')
                time.sleep(2)

            pic = pyautogui.screenshot(region=(10,90,350,200))
            width, height = pic.size
            for x in range (0, width, 2):
                for y in range (0, height, 2):
                    r,g,b = pic.getpixel((x,y))
                    if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                        if (x != 98) and (y != 44):
                            myXPosition = x
                            myYPosition = y
        pydirectinput.press('space')
        print('end')
        
    



            
def screencapMap():
    pic = pyautogui.screenshot(region=(5,90,130,65))
    pic.save(r"C:\Users\Administrator\Desktop\john\autogui\testing\연못가.png")

def runeescape():
    time.sleep(1)
    rune = pyautogui.locateOnScreen('rune.png')
    rune

def screencapRune():
    pic = pyautogui.screenshot(region=(400,200,600,100))
    pic.save(r"C:\Users\Administrator\Desktop\새 폴더\autogui\testing\runetesting.png")


def hunting(x, y, picWidth, picHeight, xMax, xMin, level):
    
    # threading.Thread(target = newWindowForVioletta).start()
    start_time = time.time()
    rooting_start_time = time.time()
    rooting = 0
    


    adjustMyXPosition = -1
    
    
    time.sleep(3)
    
    def mercedesAttackingForCoin():

        keyDownMovement()
        oneToTen = ['g','7','8','9','0','y','u','j']
        letterHolder = random.choice(oneToTen)
    
        pydirectinput.press(letterHolder)

        
        pydirectinput.press('c')
        time.sleep(.12)
        
        pydirectinput.press('c')
        time.sleep(.1)
        # letterHolder = random.choice(oneToTen)
        # pydirectinput.press(letterHolder)
        
        pydirectinput.press('c')
        time.sleep(.2)
        
        # pydirectinput.press('a')
        time.sleep(.1)
        # letterHolder = random.choice(oneToTen)
        # pydirectinput.press(letterHolder)
        pydirectinput.press('a')
        time.sleep(.8)
        
        keyUpMovement()
 
    
    def attacking(randomKey):
    
        # for random movement
        # 'c' = jump
        # 'a' = primary attack skill
        # 's' = secondary attack skill

        oneToTen = ['g','7','8','9','0','y','u','j']
        letterHolder = random.choice(oneToTen)
        

        pydirectinput.press(letterHolder)


        # elif randNumber == 5:
        #     pydirectinput.press('y')
           
        # elif randNumber == 4:
        #     pydirectinput.press('u')

        
        # elif randNumber == 5 or randNumber == 4:
        #     pydirectinput.press('q')
        #     time.sleep(.1)
        if leftOrRight == 'right':
            pydirectinput.keyDown('right')
        else: 
            pydirectinput.keyDown('left')


        pydirectinput.press('c')
        differentJumpsTiming()
        pydirectinput.press('c')
        pointOneSecond()
        pydirectinput.press(letterHolder)
        pydirectinput.press('c')
        pointOneSecond()
        
       

        pydirectinput.press('a')
        time.sleep(.575)
        
        if leftOrRight == 'right':
            pydirectinput.keyUp('right')
        else: 
            pydirectinput.keyUp('left')
        
        randomKey += 1
        


        return
    def findingMyPosition():
        pic = pyautogui.screenshot(region=(x,y,picWidth,picHeight))
        for xCurrent in range (0, width, 2):
            for yCurrent in range (0, height, 2):
                r,g,b = pic.getpixel((xCurrent,yCurrent))
                if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                        myXPosition = xCurrent
                        #print('x', myXPosition + x )
        return myXPosition
    def buffing():
        pydirectinput.press('q')
        time.sleep(.5)

        pydirectinput.press('w')
        time.sleep(1)
        pydirectinput.press('e')
        time.sleep(1)
        #pydirectinput.press('r')

        pydirectinput.press('1')
        time.sleep(1)
        
        # 7230
        pydirectinput.press('f')
        time.sleep(1)
        # pydirectinput.press('1')
        # time.sleep(1)
        # pydirectinput.press('2')
        # time.sleep(1)
        # #pydirectinput.press('4')
        # #time.sleep(1)
       
        time.sleep(.1)
    def roping():

        pydirectinput.keyDown('left')
        pydirectinput.press('c')
        time.sleep(.05)
        pydirectinput.press('c')
        time.sleep(.05)    
        pydirectinput.press('c')
        time.sleep(.2)  
        pydirectinput.press('r')
        time.sleep(2)
        pydirectinput.keyUp('left')
    def ropingRight():
        pydirectinput.keyDown('right')
        pydirectinput.press('c')
        time.sleep(.05)
        pydirectinput.press('c')
        time.sleep(.05)    
        pydirectinput.press('c')
        time.sleep(.2)  
        pydirectinput.press('r')
        time.sleep(2)
        pydirectinput.keyUp('right')

    def healthPotion():
        #health potion
        pydirectinput.press('q')
    def manaPotion():
        #mana potion
        pydirectinput.press('w')
    def jumping():
        pydirectinput.keyDown('left')
        time.sleep(.25)
        pydirectinput.press('c')
        time.sleep(.07)
        pydirectinput.keyDown('up')
        pydirectinput.press('c')
        time.sleep(.07)
        pydirectinput.press('c')
        time.sleep(.07)
        pydirectinput.keyUp('up') 
        pydirectinput.keyUp('left')
    
    def differentJumpsTiming():
        if level == 220.1:

            time.sleep(.045)
        else:
            time.sleep(.2)


        

    def goingDown():
        pydirectinput.keyDown('down')
        pydirectinput.press('c')
        time.sleep(.07)
        pydirectinput.press('c')
        time.sleep(.07)
        pydirectinput.keyUp('down')
        time.sleep(.2)
   
    def keyDownMovement():
        if leftOrRight == 'right':
            pydirectinput.keyDown('right')
        else: 
            pydirectinput.keyDown('left')
    def keyUpMovement():
        if leftOrRight == 'right':
            pydirectinput.keyUp('right')
        else: 
            pydirectinput.keyUp('left')
    def standingRoping():
        
        pydirectinput.keyDown('left')
        time.sleep(.7)
        pydirectinput.keyUp('left')
        time.sleep(.1)
        pydirectinput.press('r')
        time.sleep(.1)
    
    def pointOneSecond():
        time.sleep(.1)

    def maximunJumpingAttack():
        if leftOrRight == 'right':
            pydirectinput.keyDown('right')
        else: 
            pydirectinput.keyDown('left')
        
        randomNoise()
        pydirectinput.press('c')
        time.sleep(.2)
        pydirectinput.press('c')
        time.sleep(.15)
        randomNoise()
        pydirectinput.press('c')
        time.sleep(.15)

        pydirectinput.press('a')
        time.sleep(.8)
        if leftOrRight == 'right':
            pydirectinput.keyUp('right')
        else: 
            pydirectinput.keyUp('left')

    def randomNoise():
        oneToTen = [1,2,3,4,5,6,7,8,9,10]
        numberHolder = random.choice(oneToTen)
        randNumber = float(numberHolder)

        if randNumber == 7 or randNumber == 9:
            pydirectinput.press('g')
            # time.sleep(.1)
        elif randNumber == 8:
            pydirectinput.press('0')
            # time.sleep(.1)
        #     pydirectinput.press('a')
        #     time.sleep(.1)
        elif randNumber == 6:
            pydirectinput.press('u')
            # time.sleep(.1)
 

        


    pic = pyautogui.screenshot(region=(x,y,picWidth,picHeight))
    pic.save(r"C:\Users\Administrator\Desktop\john\autogui\testing\빙점.png")
    width, height = pic.size

    #in what floor level is the player
    

    
    leftOrRight = 'right'
    for xCurrent in range (0, width, 2):
        for yCurrent in range (0, height, 2):
            r,g,b = pic.getpixel((xCurrent,yCurrent))
            if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                    myXPosition = xCurrent
                    #print('x', myXPosition + x )
    
    while True:
        end_time = time.time() - start_time
        rooting_end_time = time.time() - rooting_start_time
        
        #skill buff
        if end_time > 190:
            buffing()
            start_time = time.time()
        
        

            
        
        #moving right
        if leftOrRight == 'right':
            if level == 215 or level == 172.9:
                    pydirectinput.keyDown('down')
                    time.sleep(.1)
                    pydirectinput.press('c')
                    time.sleep(.1)
                    pydirectinput.keyUp('down')
                    time.sleep(.1)

            while myXPosition < xMax :
                
                if level == 130 or level == 162.9 or level == 172.9:
                    mercedesAttackingForCoin()
                # elif level == 220 and rooting == 1:
                #     time.sleep(0.5)
                #     ropingRight()
                #     rooting = 0
                # elif level == 220:
                #     maximunJumpingAttack()

                


                else:
                    attacking(0)
                    
                pic = pyautogui.screenshot(region=(x,y,picWidth,picHeight))
                for xCurrent in range (0, width, 2):
                    for yCurrent in range (0, height, 2):
                        r,g,b = pic.getpixel((xCurrent,yCurrent))
                        if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                                myXPosition = xCurrent
                                #print('x', myXPosition + x )
            #healthPotion()
            # pydirectinput.press('1')
            time.sleep(0.1)
            leftOrRight = 'left'
           
                
            
            
            
           

            


            
           

        # moving left
        elif leftOrRight == 'left':
            
            
            if level == 210:
                roping()
            elif level == 215:
                
                jumping()

                if rooting_end_time > 60:
                    time.sleep(.9)
                    jumping()
                    time.sleep(.2)
                    pydirectinput.keyDown('left')
                    time.sleep(.6)
                    
                    pydirectinput.keyUp('left')
                    rooting_start_time = time.time()

            elif level == 220.1:
                if rooting_end_time > 60:
                    roping()
                    rooting_start_time = time.time()
                else:
                    standingRoping()
            
            
            elif level == 220:
                # if rooting_end_time > 60:
                pydirectinput.press('r')
                time.sleep(1.3)
                    # rooting = 1
            elif level == 172.9:
                pydirectinput.keyDown('up')
                pydirectinput.keyDown('left')
                time.sleep(.3)
                pydirectinput.keyUp('left')
                pydirectinput.press('c')
                time.sleep(.25)
                
                pydirectinput.press('c')
                time.sleep(.1)
                # letterHolder = random.choice(oneToTen)
                # pydirectinput.press(letterHolder)
                
                pydirectinput.press('c')
                time.sleep(.5)
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.keyUp('up')
                time.sleep(.7)

                
                


                

                
                

            while myXPosition > xMin:
                
                if level == 130 or level == 162.9 or level == 172.9:
                    mercedesAttackingForCoin()


                elif level == 220:
                    pic = pyautogui.screenshot(region=(70,90,50,15))
                    # pic.save(r"C:\Users\Administrator\Desktop\john\autogui\testing\ccca골드비치.png")
                    for xCurrent in range (0, 45, 1):
                        for yCurrent in range (0, 15, 1):
                            r,g,b = pic.getpixel((xCurrent,yCurrent))
                            if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                                    adjustMyXPosition = xCurrent
                                    # print(adjustMyXPosition)

                    if adjustMyXPosition  != -1:
                        while adjustMyXPosition > 20:
                            pydirectinput.keyDown('left')
                            time.sleep(.2)
                            

                            pic = pyautogui.screenshot(region=(70,90,50,15))
                            for xCurrent in range (0, 45, 1):
                                for yCurrent in range (0, 15, 1):
                                    r,g,b = pic.getpixel((xCurrent,yCurrent))
                                    if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                                            adjustMyXPosition = xCurrent
                                            # print(adjustMyXPosition)
                        pydirectinput.keyUp('left')
                        pydirectinput.keyDown('right')
                        pydirectinput.keyUp('right')
                    time.sleep(.1)
                    attacking(0)
                

                
                else:
                    attacking(0)
                

                    

                pic = pyautogui.screenshot(region=(x,y,picWidth,picHeight))
                for xCurrent in range (0, width, 2):
                    for yCurrent in range (0, height, 2):
                        r,g,b = pic.getpixel((xCurrent,yCurrent))
                        if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                                myXPosition = xCurrent
            
            leftOrRight = 'right'
            #manaPotion()

            time.sleep(0.1)

            if level == 210:
                goingDown()
            



 



# 30 - 50
def 골드비치해변():
    hunting(20, 100, 150, 65, 140, 15, 0)
    #pic = pyautogui.screenshot(region=(20,100,150,65))
    #while myXPosition < 140 
    #myXPosition > 15
    
# 64 - (75-85)
def 갱도4():
    hunting(10, 90, 140, 55, 115, 25, 0)

# 75- 100
def 관게자():
    hunting(10, 90, 170, 40, 140, 35, 0)

# 100-115
def 장남감공장():
    hunting(10,90,190,45,145,55,0)

# 125 - 130 (not recommmended)
def 여우고래():
    hunting(10,100,160,85,140,30,130)

def 까막산입구():
    hunting(0,90, 170, 110, 135, 20,130)
# 136
def 상급수련장():
    hunting(0, 90, 160, 70, 140, 50,0)
    #hunting(0, 90, 150, 100, 130, 30, 136)
    

# 160
def 암벽거인():
    hunting(0, 90, 180, 40, 165, 17, 162.9)

# 172
def 빙점의숲메르():
    hunting(0, 90, 140, 50, 125, 17, 172.9)


def 비극의숲메르():
    hunting(0, 90, 170, 60, 150, 50, 172.9)


def testing2():
    time.sleep(1)

    pydirectinput.keyDown('up')
    pydirectinput.keyDown('left')
    time.sleep(.3)
    pydirectinput.keyUp('left')
    pydirectinput.press('c')
    time.sleep(.25)
    
    pydirectinput.press('c')
    time.sleep(.1)
    # letterHolder = random.choice(oneToTen)
    # pydirectinput.press(letterHolder)
    
    pydirectinput.press('c')
    time.sleep(.5)
    pydirectinput.press('c')
    time.sleep(.1)
    pydirectinput.keyUp('up')
    



def newWindowForVioletta():
    newwindow = Toplevel(window)
    newwindow.title('비올레타')
    newwindow.geometry('800x800')

    Entry(newwindow).grid(sticky='we')
    newwindow.grid_columnconfigure(0, weight= 1)
    비올래타 = Button(newwindow, bg='blue', state= 'disabled')
    비올래타.grid(row=8, column=1, ipady=800, ipadx= 800)

    def findingVioletta():
        while True:
            if pyautogui.locateOnScreen(violetta,region=(0,0, 1050, 750), confidence= .90) != None:
                비올래타.configure(bg='red')

            
        time.sleep(5)

    
   
    threading.Thread(target=findingVioletta).start()

   





    
    
    
    


    
  
    
# 200 - 210 
def 동굴의동쪽길2():
    time.sleep(1)
    oneToTen = [1,2,3,4,5,6,7,8,9,10]
    leftAndRight = 0
    itemRoot = 0
    pic = pyautogui.screenshot(region=(20,100,220,50))
    #pic.save(r"C:\Users\Administrator\Desktop\새 폴더\autogui\testing\골드비치.png")
    width, height = pic.size
    # try for loop in whole screen
    leftOrRight = 'right'
    for x in range (0, width, 2):
        for y in range (0, height, 2):
            r,g,b = pic.getpixel((x,y))
            if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                    myXPosition = x
                    #print('x', x + 20 )
    
    while True:
        

        if leftAndRight % 6 == 0:
            pydirectinput.press('q')
            time.sleep(.5)

            pydirectinput.press('e')
            time.sleep(.5)
            
            pydirectinput.press('f')
            time.sleep(1)
            pydirectinput.press('1')
            time.sleep(.5)
            pydirectinput.press('w')
            time.sleep(1.5)
            leftAndRight += 1

        if itemRoot % 2 == 0:
            pydirectinput.press('c')
            time.sleep(.1)
            pydirectinput.press('c')
            time.sleep(.1)    
            pydirectinput.press('c')
            time.sleep(.4)  
            pydirectinput.press('r')
            time.sleep(.5)
            itemRoot += 1
        if leftOrRight == 'right':
            while myXPosition < 190:
                numberHolder = random.choice(oneToTen)
                randNumber = float(numberHolder)
                if randNumber == 7 or randNumber == 9:
                    pydirectinput.press('a')
                    time.sleep(.1)
                elif randNumber == 8:
                    pydirectinput.press('c')
                    time.sleep(.1)
                    pydirectinput.press('a')
                    time.sleep(.1)
                elif randNumber == 6:
                    pydirectinput.press('f')
                    time.sleep(.15)
                    
                pydirectinput.keyDown('right')
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('a')
                time.sleep(.7)
                pydirectinput.keyUp('right')
                pic = pyautogui.screenshot(region=(20,100,220,50))
                for x in range (0, width, 2):
                    for y in range (0, height, 2):
                        r,g,b = pic.getpixel((x,y))
                        if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                        
                            myXPosition = x
                            #print('x', x + 20 )
                           
            
            leftOrRight = 'left'
            itemRoot += 1
            #mana potion
            #pydirectinput.press('w')
        elif leftOrRight == 'left':
            while myXPosition > 15 :
                numberHolder = random.choice(oneToTen)
                randNumber = float(numberHolder)
                if randNumber == 7 or randNumber == 6:
                    pydirectinput.press('a')
                    time.sleep(.1)
                elif randNumber == 8 or randNumber == 9:
                    pydirectinput.press('c')
                    time.sleep(.1)
                    pydirectinput.press('a')
                    time.sleep(.1)
                pydirectinput.keyDown('left')
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('a')
                time.sleep(.7)
                pydirectinput.keyUp('left')
                pic = pyautogui.screenshot(region=(10,100,220,50))
                for x in range (0, width, 2):
                    for y in range (0, height, 2):
                        r,g,b = pic.getpixel((x,y))
                        if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                                myXPosition = x
            leftOrRight = 'right'
            leftAndRight += 1
            itemRoot += 1


# 210 - 200
def 길쭉동굴숲():
    hunting(10, 90, 170, 70, 160, 10, 210)


# 215 -220
def 일리야드들판():
    hunting(0, 90 , 180, 100, 165, 57, 215)

# 220 -
def 닭뛰2():
    hunting(0, 90 , 160, 60, 145, 20, 220)

def 닭뛰3():
    hunting(0, 90 , 200, 90, 180, 25, 220.1)

# 125 - 130 (not recommmended) 
def 작은연못가():
    hunting(5,90,130,65,115,15,0)
    #pic = pyautogui.screenshot(region=(5,90,130,65))
    #myXPosition < 115
    #myXPosition > 15
    start_time = time.time()

    
# restart the program
def stopping():
    #os.system('python3 "C:/Users/Administrator/Desktop/john/autogui/testing.py" ')
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    #os.execv(__file__, sys.argv)


def exitting():
    os._exit(0)

# 50 -70 (미완성)
def 조용한습지():
    time.sleep(1)
    oneToTen = [1,2,3,4,5,6,7,8,9,10]
    leftAndRight = 0
    pic = pyautogui.screenshot(region=(20,100,150,90))
    #pic.save(r"C:\Users\Administrator\Desktop\새 폴더\autogui\testing\조용한 습지.png")
    
    width, height = pic.size
    # try for loop in whole screen
    leftOrRight = 'left'
    for x in range (0, width, 2):
        for y in range (0, height, 2):
            r,g,b = pic.getpixel((x,y))
            if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                    if (x != 118) and (y != 8):
                        myXPosition = x
                        #print('x', x + 20 )
                        myYPosition = y
                        #print('y', y + 100 )

    while True:
        if leftAndRight % 6 == 0:
            pydirectinput.press('q')
            time.sleep(.5)

            pydirectinput.press('e')
            time.sleep(.5)
            
            pydirectinput.press('f')
            time.sleep(1)
            pydirectinput.press('1')
            time.sleep(.5)
            pydirectinput.press('w')
            time.sleep(1.5)
            leftAndRight += 1

       
        while myYPosition < 60 and keyboard.is_pressed('j') == False:
            numberHolder = random.choice(oneToTen)
            randNumber = float(numberHolder)
            if randNumber == 7:
                pydirectinput.press('a')
                time.sleep(.1)
            elif randNumber == 8 or randNumber == 9:
                pydirectinput.press('c')
                time.sleep(.1)
                pydirectinput.press('a')
                time.sleep(.1)
                

            else:
                pydirectinput.press('a')
                time.sleep(.2)

                pydirectinput.keyDown('down')
                time.sleep(.1)
                pydirectinput.press('c')
                time.sleep(.3)
                pydirectinput.keyUp('down')
                time.sleep(.1)
                pydirectinput.press('a')
                time.sleep(.5)

            pic = pyautogui.screenshot(region=(20,100,150,90))
            for x in range (0, width, 2):
                for y in range (0, height, 2):
                    r,g,b = pic.getpixel((x,y))
                    if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                        if (x != 118) and (y != 8):
                            myYPosition = y
                            myXPosition = x
        if myYPosition > 60:
            while myXPosition > 76 or myXPosition < 72:
                if myXPosition < 72:
                    pydirectinput.keyDown('right')
                    time.sleep(.2)
                    pydirectinput.keyUp('right')

                elif myXPosition > 76:
                    pydirectinput.keyDown('left')
                    time.sleep(.2)
                    pydirectinput.keyUp('left')
                
                
                pic = pyautogui.screenshot(region=(20,100,150,90))
                for x in range (0, width, 2):
                    for y in range (0, height, 2):
                        r,g,b = pic.getpixel((x,y))
                        if (r == 255) and ( g == 230 or g ==238) and (b ==34):
                            if (x != 118) and (y != 8):
                                myXPosition = x

            leftAndRight += 1
                    

                
                
            pydirectinput.press('up')
            pydirectinput.keyDown('left')
            time.sleep(.3)
            pydirectinput.keyUp('left')
                
            if leftOrRight == 'left':
                pydirectinput.keyDown('right')
                time.sleep(.1)
                pydirectinput.keyUp('right')
                leftOrRight = 'right'

            else:
                pydirectinput.keyDown('left')
                time.sleep(.1)
                pydirectinput.keyUp('left')
                leftOrRight = 'left'

# 코인 수급용 (까막산 입구, 삼미호, 탐사 현장 서쪽 길 2 (몹 레벨 152, 153), 암흑의 숲 1 ()
window = Tk()
window.title('메이플')
#window.geometry('700x700')

#  can't resize the program
# window.resizable(False, False)


# window.overrideredirect(1)

w = 900
h = 700

ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

x = (ws/2) - (w/8)
y = (hs/2) - (h/2)


#  adding a scrollbar 
main_frame = Frame(window)
main_frame.pack(fill= BOTH, expand = 1)
my_canvas= Canvas(main_frame)
my_canvas.pack(side=LEFT, fill= BOTH, expand = 1)
my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command= my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill= Y)
my_canvas.configure(yscrollcommand= my_scrollbar.set)
my_canvas.bind('<Configure>',  lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
final_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window= final_frame, anchor='nw')

# moving a scrollbar with mousewheel
def mouse_wheel(event):
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        my_canvas.yview_scroll(int(-1*(event.delta/120)), "unit")
    if event.num == 4 or event.delta == 120:
        my_canvas.yview_scroll(int(-1*(event.delta/120)), "unit")

window.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
window.bind("<Button-4>", mouse_wheel)
window.bind("<Button-5>", mouse_wheel)






first_frame = Frame(final_frame, width=200, height=400)
first_frame.grid(row=0, column=0, padx=(100,0), pady=5)

Label(first_frame, text = "사냥터" , font = 'Helvetica 20 bold').grid(row=0, column=0, padx=5, pady=5)

button_length = 30
Label(first_frame, text = "lv 30 - 50 " ).grid(row=1, column=0, padx=5, pady=5)
골드비치해변 = Button(first_frame, text = '골드비치 해변 2 ',  width = '25', command = threading.Thread(target=골드비치해변).start)
골드비치해변.grid(row=2, column=0, pady=(0, 10))

Label(first_frame, text = "lv 84 " ).grid(row=3, column=0, padx=5, pady=5)
갱도4 = Button(first_frame, text = '갱도4 ', width = '25',command = threading.Thread(target=갱도4).start)
갱도4.grid(row=4, column=0, pady=(0, 10))

Label(first_frame, text = "lv 95 " ).grid(row=5, column=0, padx=5, pady=5)
관게자 = Button(first_frame, text = '관게자 외 출입금지 ', width = '25',command = threading.Thread(target=관게자).start)
관게자.grid(row=6, column=0, pady=(0, 10))

Label(first_frame, text = "lv 113 " ).grid(row=7, column=0, padx=5, pady=5)
장남감공장 = Button(first_frame, text = '장남감공장<1공정> 6구역 ', width = '25',command = threading.Thread(target=장남감공장).start)
장남감공장.grid(row=8, column=0, pady=(0, 10))


Label(first_frame, text = "lv 133 " ).grid(row=9, column=0, padx=5, pady=5)
작은연못가 = Button(first_frame, text = '작은연못가 (아랫마을)(비추)', width = '25',command = threading.Thread(target=작은연못가).start)
작은연못가.grid(row=10, column=0, pady=(0, 10))

여우고래 = Button(first_frame, text = '여우고래(비추)', width = '25',command = threading.Thread(target=여우고래).start)
여우고래.grid(row=11, column=0, pady=(0, 10))

까막산입구 = Button(first_frame, text = '까막산 입구', width = '25',command = threading.Thread(target=까막산입구).start)
까막산입구.grid(row=12, column=0, pady=(0, 10))

Label(first_frame, text = "lv 136 " ).grid(row=13, column=0, padx=5, pady=5)
상급수련장 = Button(first_frame, text = '하급 수련장', width = '25',command = threading.Thread(target=상급수련장).start)
상급수련장.grid(row=14, column=0, pady=(0, 10))


Label(first_frame, text = "lv 162 " ).grid(row=15, column=0, padx=5, pady=5)
암벽거인 = Button(first_frame, text = '암벽 거인의 몸 속 2 (메르)', width = '25',command = threading.Thread(target=암벽거인).start)
암벽거인.grid(row=16, column=0, pady=(0, 10))


Label(first_frame, text = "lv 172 " ).grid(row=17, column=0, padx=5, pady=5)
빙점의숲메르 = Button(first_frame, text = '빙점의 숲2 (메르)', width = '25',command = threading.Thread(target=빙점의숲메르).start)
빙점의숲메르.grid(row=18, column=0, pady=(0, 10))


Label(first_frame, text = "lv 172 " ).grid(row=19, column=0, padx=5, pady=5)
비극의숲메르 = Button(first_frame, text = '비극의 숲2 (메르)', width = '25',command = threading.Thread(target=비극의숲메르).start)
비극의숲메르.grid(row=20, column=0, pady=(0, 10))


Label(first_frame, text = "lv 200-210 " ).grid(row=21, column=0, padx=5, pady=5)
동굴의동쪽길2 = Button(first_frame, text = '동굴의 동쪽길2 ', width = '25',command = 동굴의동쪽길2)
동굴의동쪽길2.grid(row=22, column=0, pady=(0, 10))



Label(first_frame, text = "lv 210-220 " ).grid(row=23, column=0, padx=5, pady=5)
길쭉동굴숲 = Button(first_frame, text = '길쭉 동굴숲 1 (비추)', width = '25',command = threading.Thread(target=길쭉동굴숲).start)
길쭉동굴숲.grid(row=24, column=0, pady=(0, 10))

Label(first_frame, text = "lv 215-220 " ).grid(row=25, column=0, padx=5, pady=5)
일리야드들판 = Button(first_frame, text = '일리야드 들판 4 ', width = '25',command = threading.Thread(target=일리야드들판).start)
일리야드들판.grid(row=26, column=0, pady=(0, 10))

Label(first_frame, text = "lv 220- " ).grid(row=27, column=0, padx=5, pady=5)
닭뛰2 = Button(first_frame, text = '닭이 뛰노는 곳2 ', width = '25',command = threading.Thread(target=닭뛰2).start)
닭뛰2.grid(row=28, column=0, pady=(0, 10))


Label(first_frame, text = "lv 220- " ).grid(row=29, column=0, padx=5, pady=5)
닭뛰3 = Button(first_frame, text = '닭이 뛰노는 곳3 ', width = '25',command = threading.Thread(target=닭뛰3).start)
닭뛰3.grid(row=30, column=0, pady=(0, 10))


second_frame = Frame(final_frame, width=200, height=400)
second_frame.grid(row=0, column=1, padx=(100,0), pady=5)
Label(second_frame, text = "큐브/작" , font = 'Helvetica 20 bold').grid(row=0, column=1, padx=5, pady=5)

Label(second_frame, text = "럭 9%" ).grid(row=1, column=1, padx=5, pady=5)
럭 = Button(second_frame, text = '럭 ',  width = '20')
럭.grid(row=2, column=1, pady=(0, 10))

Label(second_frame, text = "힘 9%" ).grid(row=3, column=1, padx=5, pady=5)
힘 = Button(second_frame, text = '힘 ',  width = '20')
힘.grid(row=4, column=1, pady=(0, 10))

Label(second_frame, text = "인트 9%" ).grid(row=5, column=1, padx=5, pady=5)
인트 = Button(second_frame, text = '인트 ',  width = '20')
인트.grid(row=6, column=1, pady=(0, 10))

Label(second_frame, text = "덱스 9%" ).grid(row=7, column=1, padx=5, pady=5)
덱스 = Button(second_frame, text = '덱스 ',  width = '20')
덱스.grid(row=8, column=1, pady=(0, 10))

Label(second_frame, text = "체력 9%" ).grid(row=9, column=1, padx=5, pady=5)
체력 = Button(second_frame, text = '체력 ',  width = '20')
체력.grid(row=10, column=1, pady=(0, 10))

Label(second_frame, text = "아무거나 9%" ).grid(row=11, column=1, padx=5, pady=5)
아무거나 = Button(second_frame, text = '9%',  width = '20')
아무거나.grid(row=12, column=1, pady=(0, 10))




third_frame = Frame(final_frame, width=200, height=400)
third_frame.grid(row=0, column=2, padx=(100), pady=5)


# myNote = Entry(third_frame)
# myNote.grid(row=0, column=1, padx=5, pady=5, ipady=30)

Label(third_frame, text = "그래픽은 800 x 600" ).grid(row=1, column=1, padx=5, pady=5)


Label(third_frame, text = "사냥 멈추기" ).grid(row=2, column=1, padx=5, pady=5)
stopping = Button(third_frame, text = 'stop ', command = stopping, width = '20')
stopping.grid(row=3, column=1, pady=(0, 10))


Label(third_frame, text = "나가기" ).grid(row=4, column=1, padx=5, pady=5)
exitting = Button(third_frame, text = 'exit ', command = exitting)
exitting.grid(row=5, column=1, pady=(0, 10))

testing2 = Button(third_frame, text = 'testingf' , command = testing2)
testing2.grid(row=6, column=1, pady=(0, 10))




# canvas = Canvas(third_frame, bg="yellow")
# canvas.grid(row=0, column=0, sticky="news")







window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.mainloop()