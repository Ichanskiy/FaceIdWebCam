import datetime
import sys
import cv2
import numpy as np
import os
from PIL import Image
import mysql.connector

userIdFromConsole = sys.argv[1]
pathInputImage = sys.argv[2]
# userIdFromConsole = 117
# pathInputImage = "D:/Diplom/testing/recognition/117.dsf.jpg"

print(userIdFromConsole)
print(pathInputImage)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:/Users/Ichanskiy/PycharmProjects/FaceIdWebCam/FacialRecognition/trainer/trainer.yml')
cascadePath = "C:/Users/Ichanskiy/PycharmProjects/FaceIdWebCam/FacialRecognition/Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

photoIds = set()
predictedUserID = 0

for i in range(1):
    im = Image.open(pathInputImage)
    im2arr = np.array(im)
    img = cv2.flip(im2arr, 1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        predictedUserID, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 60):
            print("predicted id = ", predictedUserID)
            photoIds.add(predictedUserID)

            confidence = "  {0}%".format(round(100 - confidence))
        else:
            predictedUserID = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        # cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        # cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    cv2.imshow('camera', img)

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
# print(studentsIds)

cnx = mysql.connector.connect(user='root', password='1111',
                              host='localhost',
                              database='attendance')
cursor = cnx.cursor()

now = datetime.datetime.now()

if (len(photoIds) == 0 or len(photoIds) >= 2):
    sql = "INSERT INTO attendance (date, presence, user_id) VALUES (%s, %s, %s)"
    val = (now, False, userIdFromConsole)

    cursor.execute(sql, val)
    cnx.commit()

for photoId in photoIds:
    # select_stmt = "SELECT id FROM students WHERE id = %(emp_no)s"
    # cursor.execute(select_stmt, { 'emp_no': photoId })
    # myresult = cursor.fetchall()
    # userId = 0
    # for x in myresult:
    #     userId = x[0]
    sql = "INSERT INTO attendance (date, presence, user_id) VALUES (%s, %s, %s)"
    print("---")
    userIdFromConsole = int(userIdFromConsole)
    predictedUserID = int(predictedUserID)
    print(userIdFromConsole)
    print(predictedUserID)
    print("---")
    if (userIdFromConsole == predictedUserID):
        val = (now, True, userIdFromConsole)
    else:
        val = (now, False, userIdFromConsole)

    cursor.execute(sql, val)
    cnx.commit()

    print(cursor.rowcount, "record inserted.")