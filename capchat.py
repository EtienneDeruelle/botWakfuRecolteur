from tensorflow import keras
import tensorflow as tf
import numpy as np
import capture
import pyautogui
import time
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

class CapchatResolver:
    img_width = 74
    img_height = 144
    
    def __init__(self):
        self.model = keras.models.load_model('model_keras/face_des')
    
    def recognizeFaceDes(self, img_file):
        img = tf.keras.utils.load_img(img_file, target_size=(self.img_width, self.img_height))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = self.model.predict(img_array)
        return tf.nn.softmax(predictions[0])

    def resolve(self, toClick):
        casesBottom = capture.parcoursBottom()
        recongnizedCasesBottom = []
        for case in casesBottom:
            recongnizedCasesBottom.append((case, np.argmax(self.recognizeFaceDes(case[0]))))
        
        casesTop = capture.parcoursTop()
        recongnizedCasesTop = []
        for case in casesTop:
            recongnizedCasesTop.append((case, np.argmax(self.recognizeFaceDes(case[0]))))
        
        face_des_to_touch = []
        for reco in recongnizedCasesBottom:
            if reco[1] != 1 and reco[1] != 3 and reco[1] != 4 and reco[1] != 11:
                face_des_to_touch.append(reco[1])
                print(str(reco[1]))
        print(face_des_to_touch)
                
        coordToClick = []
        for reco in recongnizedCasesTop:
            for face in face_des_to_touch:
                if reco[1] == face:
                    coordToClick.append(reco[0][1])
                    print(str(reco[0][1]))
                    
        if toClick:
            for i in coordToClick:
                pyautogui.moveTo(1170, 1050)
                time.sleep(5)
                pyautogui.click()
                pyautogui.moveTo(i)
                time.sleep(5)
                pyautogui.click()
        
capchatResolver = CapchatResolver()
capchatResolver.resolve(True)
    



