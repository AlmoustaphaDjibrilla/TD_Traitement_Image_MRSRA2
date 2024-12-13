import cv2
import numpy as np

# Variables globales
src = None
hsv = None
roi = None
trackbars_initialized = False

def update_trackbars(r, g, b, h, s, v):
    """Met à jour les curseurs avec les nouvelles valeurs."""
    cv2.setTrackbarPos("R", "src", r)
    cv2.setTrackbarPos("G", "src", g)
    cv2.setTrackbarPos("B", "src", b)
    cv2.setTrackbarPos("H", "src", h)
    cv2.setTrackbarPos("S", "src", s)
    cv2.setTrackbarPos("V", "src", v)

def initialize_trackbars():
    """Crée les curseurs pour RGB et HSV."""
    global trackbars_initialized
    if not trackbars_initialized:
        cv2.createTrackbar("R", "src", 0, 255, lambda x: None)
        cv2.createTrackbar("G", "src", 0, 255, lambda x: None)
        cv2.createTrackbar("B", "src", 0, 255, lambda x: None)
        cv2.createTrackbar("H", "src", 0, 180, lambda x: None)
        cv2.createTrackbar("S", "src", 0, 255, lambda x: None)
        cv2.createTrackbar("V", "src", 0, 255, lambda x: None)
        trackbars_initialized = True

def on_mouse_zoom_img(event, x, y, flags, param):
    """Callback pour capturer les événements de souris."""
    global src, hsv, roi

    if event == cv2.EVENT_LBUTTONDOWN:
        # Mise à jour des valeurs de la région pointée
        if roi is not None:
            X = roi[0] + x
            Y = roi[1] + y
            b, g, r = src[Y, X]
            h, s, v = hsv[Y, X]
            update_trackbars(int(r), int(g), int(b), int(h), int(s), int(v))

def main():
    global src, hsv, roi

    # Charger l'image
    src = cv2.imread("pic2.png")
    if src is None:
        print("Erreur : Impossible de charger l'image !")
        return

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    roi = (0, 0, src.shape[1], src.shape[0])  # Région par défaut

    # Créer la fenêtre et les trackbars
    cv2.namedWindow("src")
    initialize_trackbars()

    # Associer le callback de la souris
    cv2.setMouseCallback("src", on_mouse_zoom_img)

    while True:
        cv2.imshow("src", src)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Touche Échap pour quitter
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
