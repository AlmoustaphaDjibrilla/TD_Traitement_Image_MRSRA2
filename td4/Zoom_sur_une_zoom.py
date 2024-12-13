import cv2
import numpy as np

# Variables globales
src = None
roi = None

def on_mouse_zoom_img(event, x, y, flags, param):
    global src, roi
    if roi is not None:
        X = roi[0] + x
        Y = roi[1] + y
        # Obtenir les valeurs RGB
        b, g, r = src[Y, X]
        # Mettre à jour les curseurs (si vous utilisez une interface GUI, ajoutez des trackbars)
        print(f"R: {r}, G: {g}, B: {b}")

def main():
    global src, roi
    src = cv2.imread("pic2.png")
    if src is None:
        print("Image non chargée!")
        return

    # Définir une région d'intérêt par défaut
    roi = (0, 0, src.shape[1], src.shape[0])  # x, y, largeur, hauteur

    # Créer une fenêtre et associer le callback
    cv2.namedWindow("src")
    cv2.setMouseCallback("src", on_mouse_zoom_img)

    while True:
        cv2.imshow("src", src)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Touche Échap pour quitter
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
