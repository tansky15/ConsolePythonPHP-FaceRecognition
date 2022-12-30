import numpy as np
import face_recognition
from os import listdir
import os
import cv2
from datetime import datetime
from gtts import gTTS
import os
import socket
import requests

from Domain.LocalizedByIP import *
from Domain.Camera import *
from Domain.GeoMap import *

import IP2Location


# get the ip adress
hostname = socket.gethostname()
ipAdress = socket.gethostbyname(hostname)

# get the geo-localisation
getip = get_location(ipAdress)
myLocalisation = GeoMap(getip.get("latitude"),
                        getip.get("longitude"))



# set the box
myBox = Camera("camera chambre personnel", ipAdress, myLocalisation)

# Variables globales
path = 'Images/'
images = []
classNames = []
myList = listdir(path)
# read iamges from the folder

for cl in myList:
    # print(f'{path}'/{cl}')
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    # par defaut le separateur est le point
    # cl est le nom de l'image


# Find face and compute encodings(features)
def findEncoding(myImgs):
    encodeList = []
    for myImg in myImgs:
        img = cv2.cvtColor(myImg, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListFinal = findEncoding(images)
print('Images encoded successfully !')

# read Image from webcam
cap = cv2.VideoCapture(1)
while True:
    success, img = cap.read()
    if success:
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # resize
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # Find face location of the webcam
        facesCurFrame = face_recognition.face_locations(imgS)
        # Encode face
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            print("il ya quelqu'un a la maison")
            matches = face_recognition.compare_faces(
                encodeListFinal, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListFinal, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                myBox.SignalerSuspect(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2),
                              (0, 255, 0), 2)  # RGB #bordure
                cv2.rectangle(img, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+10, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow(myBox.getCameraName(), img)
        cv2.waitKey(1)
