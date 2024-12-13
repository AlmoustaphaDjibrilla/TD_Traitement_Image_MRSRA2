import cv2
import numpy as np

# Callback pour afficher le profil d'intensité
def cb_intensity_profile(pos):
    global src, dst, y_im_profile

    # Copier l'image source
    dst = src.copy()

    # Dessiner une ligne blanche sur l'image
    cv2.line(dst, (0, pos), (src.shape[1], pos), (255, 255, 255), 3)
    cv2.imshow("stuff", dst)

    # Extraire la ligne sélectionnée
    y_profile = src[pos, :]

    # Réinitialiser l'image du profil
    y_im_profile.fill(255)
    H = y_im_profile.shape[0]

    # Tracer le profil sur une nouvelle image
    for i in range(len(y_profile) - 1):
        val = y_profile[i]
        val2 = y_profile[i + 1]
        cv2.line(y_im_profile, (i, H - val), (i + 1, H - val2), (0, 0, 0), 2)

    cv2.imshow("Y intensity profile", y_im_profile)

# Charger une image en niveaux de gris
src = cv2.imread("stuff.jpg", 0)
height, width = src.shape

# Préparer des images pour l'affichage
dst = src.copy()
y_im_profile = np.full((256, width), 255, dtype=np.uint8)

# Créer une fenêtre avec un curseur
cv2.namedWindow("stuff")
cv2.createTrackbar("Y position", "stuff", 40, height - 1, cb_intensity_profile)

# Afficher l'image source
cv2.imshow("stuff", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
