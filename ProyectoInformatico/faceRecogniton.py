import cv2 
import face_recognition


#captura de video
cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)#indico que voy a capturar un video y ocupe toda la ventana
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count = 0

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        for face_loc in face_locations:
            #face_loc = face_recognition.face_locations(frame)[0]
            face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_loc])[0]
            results = face_recognition.compare_faces([face_frame_encodings], face_image_encodings)
            if results[0]:
                cv2.rectangle(frame, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 0), 2)
                cv2.putText(frame, "Match Found", (face_loc[3], face_loc[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow("Video", frame)
    k=cv2.waitKey(30)
    if k == 27 & 0xFF:
        break


cap.release()