import cv2
import numpy as np

def main():
    # Charger l'image
    src = cv2.imread("pic2.png")
    if src is None:
        print("Erreur : Impossible de charger l'image !")
        return

    # Conversion en HSV
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    hue, saturation, _ = cv2.split(hsv)

    # Paramètres de l'histogramme 2D
    h_bins, s_bins = 32, 32
    h_range = [0, 180]
    s_range = [0, 255]
    hist_size = [h_bins, s_bins]
    ranges = [h_range, s_range]

    # Calcul de l'histogramme 2D
    hist = cv2.calcHist([hue, saturation], [0, 1], None, hist_size, ranges)
    hist = cv2.normalize(hist, hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Création d'une image pour afficher l'histogramme
    scale = 10
    hist_image = np.zeros((s_bins * scale, h_bins * scale, 3), dtype=np.uint8)

    for h in range(h_bins):
        for s in range(s_bins):
            bin_val = hist[s, h]
            intensity = int(bin_val)
            cv2.rectangle(hist_image, 
                          (h * scale, s * scale), 
                          ((h + 1) * scale - 1, (s + 1) * scale - 1), 
                          (intensity, intensity, intensity), 
                          thickness=cv2.FILLED)

    # Afficher l'image de l'histogramme
    cv2.imshow("Histogramme H-S", hist_image)
    cv2.imshow("Image Source", src)

    # Attendre une touche et fermer
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
