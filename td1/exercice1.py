import cv2
import numpy as np
import random

# Dimensions de l'image
hauteur, largeur = 480, 640

# Fonction pour remplir l'image
def remplir_image(image, couleur):
    image[:, :] = couleur

# Fonction pour dessiner un rectangle
def dessiner_rectangle(image, couleur):
    centre_x, centre_y = largeur // 2, hauteur // 2
    top_left = (centre_x - 25, centre_y - 50)
    bottom_right = (centre_x + 25, centre_y + 50)
    cv2.rectangle(image, top_left, bottom_right, couleur, -1)

# Création de l'image
image = np.zeros((hauteur, largeur, 3), dtype=np.uint8)

while True:
     cv2.imshow("Image", image)
     key = cv2.waitKey(0) & 0xFF
     if key == ord('n'):  # Touche 'n'
        remplir_image(image, (0, 0, 0))
     elif key == ord('c'):  # Touche 'c'
        couleur = tuple(random.randint(0, 255) for _ in range(3))
        remplir_image(image, couleur)
     elif key == ord('r'):  # Touche 'r'
        couleur = tuple(random.randint(0, 255) for _ in range(3))
        dessiner_rectangle(image, couleur)
     elif key == 27:  # Touche 'Esc'
        break

cv2.destroyAllWindows()