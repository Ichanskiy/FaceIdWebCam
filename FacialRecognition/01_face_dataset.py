import re

import cv2
import os
import numpy as np
from PIL import Image

id = 1
count = 10
dirPath = ""
listFiles = []

for (dirPath, dirnames, filenames) in os.walk(
        # "C:/Users/Ichanskiy/PycharmProjects/FaceIdWebCam/FacialRecognition/input/"):
        "D:/Diplom/testing/input/"):
    listFiles = filenames
    print(list)
    print(dirPath)
    print(dirnames)
    break

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

listFiles.sort(reverse=True)
for fileName in listFiles:
    im = Image.open(dirPath + fileName)
    idImage = fileName.replace(".jpg", "")
    idImage = re.findall("\d+", idImage)[0]
    im2arr = np.array(im)

    img = cv2.flip(im2arr, 1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for i in range(1, count):
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Save the captured image into the datasets folder
            # cv2.imwrite("C:/Users/Ichanskiy/PycharmProjects/FaceIdWebCam/FacialRecognition/dataset/" + str(
            cv2.imwrite("D:/Diplom/testing/dataset/" + str(
                idImage) + '.' + str(i) + ".jpg", gray[y:y + h, x:x + w])
            # count += 1
    id = id + 1
