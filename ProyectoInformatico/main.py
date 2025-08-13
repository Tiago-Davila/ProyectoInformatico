import cv2 
import os
#import imutils


if not os.path.exists('Rostros encontrados'):
    print('Creando carpeta "Rostros encontrados"')#hago directorio si no existe la carpeta
    os.makedirs('Rostros encontrados')


cap= cv2.VideoCapture(1, cv2.CAP_DSHOW)#indico que voy a capturar un video y ocupe toda la ventana
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo leer el frame de la cámara.")
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy() #copia de la imagen original
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    k=cv2.waitKey(30) 
    if k == 27:#codigo asci 'esc'
        break
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        if k == ord('s') or count <=10 :
            count += 1
            cv2.imwrite('Rostros encontrados/rostro_{}.jpg'.format(count), rostro)
            print('rostro_{}.jpg guardado'.format(count))
            cv2.imshow('Video', frame)
    cv2.rectangle(frame, (10, 5), (450, 25), (255, 255, 255), -1)
    cv2.putText(frame, 'Presiona "s" para guardar el rostro', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.imshow('Video', frame)


cap.release()