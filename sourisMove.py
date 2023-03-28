import pyautogui
import time

widthCase = 142
heightCase = 72

def moveCenter(widthAdjustement:int, heightAdjustement:int):
    centre = (960,540)
    pyautogui.moveTo(centre[0] +widthAdjustement, centre[1] + heightAdjustement)

def moveRightBottom():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x + widthCase/2 , positionSouris.y + heightCase/2)

def moveRightTop():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x + widthCase/2 , positionSouris.y - heightCase/2)
    
def moveLeftTop():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x - widthCase/2 , positionSouris.y - heightCase/2)

def moveLeftBottom():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x - widthCase/2 , positionSouris.y + heightCase/2)
    
def moveLeft():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x - widthCase, positionSouris.y)
    
def moveRight():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x + widthCase, positionSouris.y)

def moveTop():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x, positionSouris.y - heightCase)

def moveBottom():
    positionSouris = pyautogui.position()
    pyautogui.moveTo(positionSouris.x, positionSouris.y + heightCase)
    
    
def moveSide(number):
    if(number == 0): 
        moveLeft()
    if(number == 1): 
        moveTop()
    if(number == 2): 
        moveRight()
    if(number == 3): 
        moveBottom()


#def moveCercleUntil(rayonCercle :int, timeToWait :int, imagePath:any):
#    nbCote = 4
#    for i in range(rayonCercle):
#        time.sleep(timeToWait)
#        moveRightBottom()
#        for j in range(nbCote):
#            for k in range(i+1):
#                time.sleep(timeToWait)
#                moveSide(j)
#                im = pyautogui.locateOnScreen(imagePath, confidence=0.8)
#                if im :
#                    return True
#    return False

def moveCercleUntil(rayonCercle :int, timeToWait :int, functionCondition:any):
    nbCote = 4
    for i in range(rayonCercle):
        time.sleep(timeToWait)
        moveRightBottom()
        for j in range(nbCote):
            for k in range(i+1):
                time.sleep(timeToWait)
                moveSide(j)
                cond = functionCondition()
                if cond :
                    return True
    return False