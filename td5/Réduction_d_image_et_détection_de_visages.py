from tkinter import CASCADE
import cv2
# Réduction de l'image
scale = 2
temp = cv2.pyrDown(src)

# Détection des visages sur l'image réduite
faces = CASCADE.detectMultiScale(temp, scaleFactor=1.2, minNeighbors=2)

# Dessin des rectangles autour des visages détectés
for (x, y, w, h) in faces:
    cv2.rectangle(src, (x*scale, y*scale), ((x+w)*scale, (y+h)*scale), (0, 0, 255), 3)

# Affichage des résultats
cv2.imshow("Detection", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
