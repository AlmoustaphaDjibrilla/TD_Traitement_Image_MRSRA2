import cv2

# Chargement de la cascade
cascade_name = "haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_name)

# Chargement de l'image
src = cv2.imread("lena.jpg")

# Détection des visages
faces = cascade.detectMultiScale(src, scaleFactor=1.2, minNeighbors=5)

# Dessin des rectangles autour des visages détectés
for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y), (x+w, y+h), (255, 255, 255), 1)

# Affichage des résultats
cv2.imshow("Detection", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
