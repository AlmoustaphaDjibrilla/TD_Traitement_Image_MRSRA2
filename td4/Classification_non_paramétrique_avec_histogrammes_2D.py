import cv2
import numpy as np

def main():
    # Charger une image et convertir en HSV
    src = cv2.imread("pic2.png")
    if src is None:
        print("Erreur : Impossible de charger l'image !")
        return

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    hue, saturation, _ = cv2.split(hsv)

    # Apprentissage : histogramme 2D (exemple de données d'apprentissage)
    h_bins, s_bins = 32, 32
    hist_size = [h_bins, s_bins]
    h_range, s_range = [0, 180], [0, 255]
    ranges = [h_range, s_range]

    # Construire l'histogramme 2D à partir d'une zone de peau (exemple)
    mask = cv2.inRange(hsv, (0, 50, 50), (20, 255, 255))  # Exemple : pixels peau dans H-S
    hs_planes = [hue, saturation]
    hist = cv2.calcHist(hs_planes, [0, 1], mask, hist_size, ranges)
    hist = cv2.normalize(hist, hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Rétroprojection de l'histogramme sur l'image complète
    back_proj = cv2.calcBackProject(hs_planes, [0, 1], hist, ranges, scale=1)

    # Application d'un filtre pour améliorer le masque
    back_proj = cv2.GaussianBlur(back_proj, (5, 5), 0)

    # Affichage des résultats
    cv2.imshow("Image Source", src)
    cv2.imshow("Histogramme BackProjection", back_proj)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
