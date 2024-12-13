import cv2

# Charger une vidéo
capture = cv2.VideoCapture("traffic.avi")

frame_number = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Sauvegarder chaque trame
    frame_filename = f"frame_{frame_number}.jpg"
    cv2.imwrite(frame_filename, frame)

    frame_number += 1

capture.release()
