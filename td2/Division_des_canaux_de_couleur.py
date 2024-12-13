import cv2

# Charger l'image
image = cv2.imread("atlas-v-rocket-vandenberg-air-force-base-1920x1080_97495-mm-90.jpg")

# Séparer les canaux
b, g, r = cv2.split(image)

# Afficher les canaux
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

# Sauvegarder les canaux
cv2.imwrite("lena_B.bmp", b)
cv2.imwrite("lena_G.jpg", g)
cv2.imwrite("lena_R.jpg", r)
cv2.imwrite("LenaColor.png", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
