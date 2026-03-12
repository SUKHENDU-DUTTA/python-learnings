import cv2
face_capture = cv2.CascadeClassifier('C:/Users/Sukhendu/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
while True:
    ret, video_data = video_capture.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_capture.detectMultiScale(col, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0,255, 0), 2)
    cv2.imshow('Video_live', video_data)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
video_capture.release()