import cv2

#Insert the name of the video you want the program to execute
cap = cv2.VideoCapture('people_-_6387 (720p).mp4')

#Using OpenCV to detect bodies
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while(True):
    ret, frame = cap.read()

    if frame is None:
        print("El video ha terminado")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.05, 2) 
    # The value "1.05": A smaller value, such as 1.05 or 1.1, will cause objects 
    # to be searched for in a wider range of sizes, but it can also make detection 
    # slower and less accurate. A larger value, such as 1.2 or 1.3, will make 
    # detection faster but potentially less sensitive to objects of different sizes.

    # The value "2": It will require a greater match between rectangles before 
    # considering an object. A lower value will make detection more sensitive 
    # but can also generate more false positives.

    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Human Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
