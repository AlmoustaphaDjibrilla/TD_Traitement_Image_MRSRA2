import cv2

# Initialiser la capture depuis la webcam
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Afficher le flux vidéo
    cv2.imshow("Webcam", frame)

    # Quitter avec une touche
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()