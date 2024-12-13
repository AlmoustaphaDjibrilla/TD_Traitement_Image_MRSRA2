import cv2

def main():
    # Charger l'image source
    src = cv2.imread("pic2.png")
    if src is None:
        print("Erreur : Impossible de charger l'image !")
        return

    # Conversion en différents espaces colorimétriques
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    ycbcr = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Affichage des images
    cv2.imshow("Image Source (BGR)", src)
    cv2.imshow("Image HSV", hsv)
    cv2.imshow("Image YCbCr", ycbcr)
    cv2.imshow("Image Niveau de Gris", gray)

    # Attendre une touche pour fermer
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
