import time

import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.C:\Users\Ichanskiy\PycharmProjects\video_streaming_with_flask_example\templates
        # time.sleep(5)
        ret, jpeg = cv2.imencode('.jpg', image)
        cv2.imwrite(cv2.os.path.join("D:/Diplom/registration", "user.png"), image)

        return jpeg.tobytes()