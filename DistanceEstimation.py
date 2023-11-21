import cv2

HaarCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = HaarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h
        print("diaginal point 1 (x1,y1) = ({},{})".format(x1, y1))
        print("diaginal point 2 (x2,y2) = ({},{})".format(x2, y2))
        cv2.rectangle(frame, (x, y), (x + w, y + h),
                      (0, 255, 0), 2)
        cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
