import cv2

#Insert the name of the video you want the program to execute
cap = cv2.VideoCapture('people_-_6387 (720p).mp4')

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while(True):
    ret, frame = cap.read()

    if frame is None:
        print("El video ha terminado")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.2, 3)

    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Human Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
