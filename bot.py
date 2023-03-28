import pyautogui
import time
import sourisMove
import capchat

widthAdjustementGraineMelon = 5
heightAdjustementGraineMelon = 0
widthAdjustementMelon = -10
heightAdjustementMelon = 10
widthAdjustementPlantageMelon = 35
heightAdjustementPlantageMelon = 0
rayonCercle = 6
nbCote = 4

def recenterSouris(widthAdjustement:int, heightAdjustement:int):
    sourisMove.moveCenter(widthAdjustement, heightAdjustement)


### RECOLTE GRAINE DE MELON
def findMelonWithGraine():
    melon = pyautogui.locateOnScreen("capture/melon_name.png", confidence=0.8)
    if melon:
        pyautogui.rightClick()
        hand = pyautogui.locateOnScreen("capture/main_recolte.png")
        if hand:
            pyautogui.moveTo(hand)
            return True
        else:
            return False
    else:
        return False

def recolteGraineMelon(nbRecolte:int):
    recenterSouris(widthAdjustementGraineMelon, heightAdjustementGraineMelon)
    for i in range(nbRecolte):
        melonFind = sourisMove.moveCercleUntil(rayonCercle, 0.3, findMelonWithGraine)
        if melonFind:
            pyautogui.click()
            time.sleep(7)
            recenterSouris(widthAdjustementGraineMelon, heightAdjustementGraineMelon)


### RECOLTE MELON
def findMelonWithoutGraine():
    melon = pyautogui.locateOnScreen("capture/melon_name.png", confidence=0.8)
    if melon:
        pyautogui.rightClick()
        hand = pyautogui.locateOnScreen("capture/main_recolte.png")
        cisaille = pyautogui.locateOnScreen("capture/cisaille.png")
        if hand:
            return False
        else:
            if cisaille:
                pyautogui.moveTo(cisaille)
                return True
            else:
                return False
    else:
        return False
                
def findMelonNimp():
    melon = pyautogui.locateOnScreen("capture/melon_name.png", confidence=0.8)
    if melon:
        pyautogui.rightClick()
        cisaille = pyautogui.locateOnScreen("capture/cisaille.png")
        if cisaille:
            pyautogui.moveTo(cisaille)
            return True
    else:
        return False
                
# nimp : argument booleen permettant de dire à la fonction de récolté un melon peu importe son état
def recolteMelon(nbRecolte:int, nimp:bool):
    recenterSouris(widthAdjustementMelon, heightAdjustementMelon)
    for i in range(nbRecolte):
        melonFind = sourisMove.moveCercleUntil(rayonCercle, 0.3, findMelonNimp if nimp else findMelonWithoutGraine)
        if melonFind:
            pyautogui.click()
            time.sleep(7)
            recenterSouris(widthAdjustementMelon, heightAdjustementMelon)
            
### PLANTAGE MELON
def findTerrePlantage():
    zoneMeuble = pyautogui.locateOnScreen("capture/soixante_pourcent.png", confidence=0.8)
    #zone_meuble4
    if zoneMeuble:
        return True
    else:
        return False
def plantageMelon(nbPlantage:int):
    selectGraine()
    recenterSouris(widthAdjustementPlantageMelon, heightAdjustementPlantageMelon)
    for i in range(nbPlantage):
        zonePlantageFind = sourisMove.moveCercleUntil(rayonCercle, 0.3, findTerrePlantage)
        if zonePlantageFind:
            pyautogui.click()
            time.sleep(4)
            selectGraine()
            recenterSouris(widthAdjustementPlantageMelon, heightAdjustementPlantageMelon)

def selectGraine():
    pyautogui.moveTo(1090, 1050)
    pyautogui.click()


capchatResolver = capchat.CapchatResolver()
numPassage = 0
while(True):
    numPassage += 1
    print('Passage numéro {}'.format(numPassage))
    recolteGraineMelon(30)
    
    recolteMelon(30, True)
    
    plantageMelon(50)