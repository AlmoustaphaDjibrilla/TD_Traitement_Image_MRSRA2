import cv2

# Initialiser la capture depuis la webcam
capture = cv2.VideoCapture(0)

# Définir le codec et créer le fichier de sortie
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Écrire chaque frame dans la vidéo
    out.write(frame)

    # Afficher le flux vidéo
    cv2.imshow("Webcam", frame)

    # Quitter avec une touche
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()
