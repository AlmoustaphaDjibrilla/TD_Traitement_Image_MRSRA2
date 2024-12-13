from tkinter import CASCADE
import cv2

# Chargement de la vidéo
capture = cv2.VideoCapture("visionface.mp4")

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Détection des visages
    faces = CASCADE.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=5)

    # Dessin des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

    # Affichage
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) >= 0:
        break

capture.release()
cv2.destroyAllWindows()
