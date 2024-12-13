import cv2

# Charger l'image
image = cv2.imread("atlas-v-rocket-vandenberg-air-force-base-1920x1080_97495-mm-90.jpg")

# Afficher l'image
cv2.imshow("atlas-v-rocket-vandenberg-air-force-base-1920x1080_97495-mm-90", image)

# Pause jusqu'à appuyer sur une touche
cv2.waitKey(0)

# Fermer toutes les fenêtres
cv2.destroyAllWindows()
