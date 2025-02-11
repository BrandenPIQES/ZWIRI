'''
This detects the motion of anything that that appears in front of the camera
it uses uses contours to track the motion 
'''

import cv2


class MotionDetector():
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
        self.eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
        self.video = cv2.VideoCapture(0)
        self.first_frame = None

    def detect_motion(self):
        cv2.namedWindow('intruder', cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty('intruder', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:
            check, frame = self.video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

            eyes = self.eye_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)
            for (x, y, w, h) in eyes:
                cv2.circle(frame, (x, y), 10, (255, 255, 255), 4, None, None)

            if self.first_frame is None:
                self.first_frame = gray
                continue
            delta_frame = cv2.absdiff(self.first_frame, gray)
            threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
            threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

            (cntr, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in cntr:
                if cv2.contourArea(contour) < 1000:
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.circle(frame, (x, y), 10, (0, 0, 255), 4, None, None)

            cv2.imshow('intruder', frame)
            key = cv2.waitKey(1)
            if key == ord('q') or key == ord("Q"):
                break

        self.video.release()
        cv2.destroyAllWindows()

# Usage
motion_detector = MotionDetector()

