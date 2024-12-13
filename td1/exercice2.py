import cv2
import numpy as np

# Dimensions de l'image
hauteur, largeur = 480, 640

# Variables globales
dessiner = False
longueur, largeur_rect = 50, 100

# Fonction pour dessiner un rectangle
def dessiner_rectangle(image, longueur, largeur):
    centre_x, centre_y = largeur // 2, hauteur // 2
    top_left = (centre_x - largeur // 2, centre_y - longueur // 2)
    bottom_right = (centre_x + largeur // 2, centre_y + longueur // 2)
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), -1)

# Callback pour les sliders
def update_longueur(value):
    global longueur
    longueur = value

def update_largeur(value):
    global largeur_rect
    largeur_rect = value

# Création de l'image
image = np.zeros((hauteur, largeur, 3), dtype=np.uint8)

cv2.namedWindow("Image")
cv2.createTrackbar("Longueur", "Image", 50, 200, update_longueur)
cv2.createTrackbar("Largeur", "Image", 100, 200, update_largeur)

while True:
    temp_image = image.copy()
    if dessiner:
        dessiner_rectangle(temp_image, longueur, largeur_rect)
    cv2.imshow("Image", temp_image)
    key = cv2.waitKey(30) & 0xFF
    if key == ord('r'):
        dessiner = not dessiner
    elif key == 27:  # Touche 'Esc'
        break

cv2.destroyAllWindows()