import pyautogui
import random
import time
import uuid
import skimage
from skimage import io as io_skimage
import numpy
import sys
import tensorflow as tf

global fileNumber
fileNumber = 0

width = 144
height = 74
positionX = 890
positionY = 200
nbScreenShot = 10

rayonCercle = 5

widthCase = 142
heightCase = 71

def moveLeft(pos):
    return (pos[0]- widthCase, pos[1])
    
def moveRight(pos):
    return (pos[0]+ widthCase, pos[1])

def moveTop(pos):
    return (pos[0], pos[1] - heightCase)

def moveBottom(pos):
    return (pos[0],pos[1] + heightCase)

def moveRightBottom(pos):
    return (pos[0] + widthCase/2 ,pos[1] + heightCase/2)

def moveRightTop(pos):
    return (pos[0] + widthCase/2 ,pos[1] - heightCase/2)

def moveLeftBottom(pos):
    return (pos[0] - widthCase/2 ,pos[1] + heightCase/2)

def moveLeftTop(pos):
    return (pos[0] - widthCase/2 ,pos[1] - heightCase/2)
    
    
def moveSide(number, pos):
    if(number == 0): 
        return moveLeftTop(pos)
    if(number == 1): 
        return moveRightTop(pos)
    if(number == 2): 
        return moveRightBottom(pos)
    if(number == 3): 
        return moveLeftBottom(pos)

def screenshotAll(rayonCercle :int, timeToWait :int, pos):
    nbCote = 4
    #pyautogui.moveTo(pos)
    for i in range(rayonCercle):
        time.sleep(timeToWait)
        pos= moveBottom(pos)
        #pyautogui.moveTo(pos)
        for j in range(nbCote):
            for k in range((i+1)*2):
                time.sleep(timeToWait)
                pos = moveSide(j, pos)
                #pyautogui.moveTo(pos)
                takeScreenShot(pos)
    return False

def takeScreenShot(pos):
    for i in range(1):
        global fileNumber
        fileNumber +=1
        nomFichier = "dataset/essai/%s.png" % (str(fileNumber))
        time.sleep(1)
        numpy.set_printoptions(threshold=sys.maxsize)
        print(nomFichier)
        pyautogui.screenshot(nomFichier,region=(pos[0]+13, pos[1]+15, width, height))# +13    +15
        image_entre = io_skimage.imread(nomFichier)
        #print(image_entre)
        image_entre = numpy.dstack((image_entre, numpy.ones((height, width), dtype=int)*255))
        #rgba = numpy.concatenate((image_entre, numpy.zeros((205, 54, 1))), axis=2)
        #print(image_entre)
        image_gabarit = io_skimage.imread("gabarit_alpha.png")
        #print(image_gabarit)
        image_sortie = image_entre-image_gabarit
        #image_sortie[image_sortie<0] = 255
        #print(image_sortie)
        io_skimage.imsave(nomFichier, image_sortie)
        

def parcoursBottom():
    list = []
    sourisPosition = getCenterPosition()
    sourisPosition= moveBottom(sourisPosition)
    sourisPosition= moveBottom(sourisPosition)
    sourisPosition= moveLeftBottom(sourisPosition)
    sourisPosition= moveLeftBottom(sourisPosition)
    sourisPosition= moveLeftBottom(sourisPosition)
    list.append((screenshot('bottom', sourisPosition), sourisPosition))
    for y in range(1,3):
        for i in range(10):
            sourisPosition= moveRightTop(sourisPosition)
            list.append((screenshot('bottom', sourisPosition), sourisPosition))
        
        sourisPosition= moveRightBottom(sourisPosition)
        list.append((screenshot('bottom', sourisPosition), sourisPosition))
        
        for i in range(10):
            sourisPosition= moveLeftBottom(sourisPosition)
            list.append((screenshot('bottom', sourisPosition), sourisPosition))
        
        sourisPosition= moveRightBottom(sourisPosition)
        list.append((screenshot('bottom', sourisPosition), sourisPosition))
        
    for i in range(10):
        sourisPosition= moveRightTop(sourisPosition)
        list.append((screenshot('bottom', sourisPosition), sourisPosition))
    return list
        
def parcoursTop():     
    list = []
    sourisPosition = getCenterPosition()
    sourisPosition= moveTop(sourisPosition)
    sourisPosition= moveRightTop(sourisPosition)
    sourisPosition= moveRightTop(sourisPosition)
    sourisPosition= moveRightTop(sourisPosition)
    sourisPosition= moveRightTop(sourisPosition)
    list.append((screenshot('top', sourisPosition), sourisPosition))
    for y in range(1,3):
        for i in range(10):
            sourisPosition= moveLeftBottom(sourisPosition)
            list.append((screenshot('top', sourisPosition), sourisPosition))
        
        sourisPosition= moveLeftTop(sourisPosition)
        list.append((screenshot('top', sourisPosition), sourisPosition))
        
        for i in range(10):
            sourisPosition= moveRightTop(sourisPosition)
            list.append((screenshot('top', sourisPosition), sourisPosition))
        
        sourisPosition= moveLeftTop(sourisPosition)
        list.append((screenshot('top', sourisPosition), sourisPosition))
        
    for i in range(10):
        sourisPosition= moveLeftBottom(sourisPosition)
        list.append((screenshot('top', sourisPosition), sourisPosition))
    return list
        

def screenshot(folder, pos):
    global fileNumber
    fileNumber +=1
    uuidString = str(uuid.uuid4())
    nomFichier = "tmp/%s/%s-%s.png" % (folder, uuidString, str(fileNumber))
    #numpy.set_printoptions(threshold=sys.maxsize)
    pyautogui.screenshot(nomFichier,region=(pos[0]-67, pos[1]-32, width, height))# +13    +15
    image_entre = io_skimage.imread(nomFichier)
    image_entre = numpy.dstack((image_entre, numpy.ones((height, width), dtype=int)*255))
    image_gabarit = io_skimage.imread("gabarit_alpha.png")
    image_sortie = image_entre-image_gabarit
    io_skimage.imsave(nomFichier, image_sortie)
    return nomFichier


def getCenterPosition():
    bottePosition = pyautogui.locateCenterOnScreen('capture/chat.png', confidence=0.8)
    if bottePosition == None:
        print('No botte repered')
        #bottePosition = (960, 540)
    bottePosition = moveLeftTop(bottePosition)
    #bottePosition = moveRightBottom(bottePosition)
    #bottePosition = moveRightBottom(bottePosition)
    return bottePosition