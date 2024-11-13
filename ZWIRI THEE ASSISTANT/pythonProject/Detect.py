import cv2


face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')

video = cv2.VideoCapture(0)  # zero coz I'm using my laptop front cam which is the first opt if there were other cams
# i would have said 1 or 2 depending on which one comes first

# Create a named window and set it to fullscreen
cv2.namedWindow('intruder', cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty('intruder', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

first_frame = None

while True:  # I want the video to play continuously, since a video is just a sequence of images/ images on a very
    # fast slide show
    check, frame = video.read()  # reading data extracted by "video" variable
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converting the video colour to gray to improve the accuracy of
    # the
    # video to be read
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # BLUR THE VIDEO SO THAT MOTION CAN BE DETECTED EASILY

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, flags=None, minSize=None,  maxSize=None)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, flags=None, minSize=None, maxSize=None)

    for (x, y, w, h) in eyes:
        cv2.circle(frame, (x, y), 10, (255, 255, 255), 4, None, None)

    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame, gray)
    threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    (cntr, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame, (x, y), 50, (0, 0, 255), 4, None, None)

    cv2.imshow('intruder', frame)
    key = cv2.waitKey(1)
    if key == ord('q') or key == ord("Q"):
        break

video.release()
cv2.destroyAllWindows()
