import cv2
import numpy as np

def mahalanobis_probability(color, mean, cov_inv):
    """
    Calcule une probabilité basée sur la distance de Mahalanobis.
    :param color: Vecteur couleur (R, G, B).
    :param mean: Moyenne des couleurs de peau.
    :param cov_inv: Inverse de la matrice de covariance.
    :return: Probabilité (0 à 1).
    """
    diff = color - mean
    dist = np.dot(np.dot(diff.T, cov_inv), diff)
    probability = np.exp(-0.5 * dist)  # Loi normale : exp(-d²/2)
    return probability

def main():
    # Charger l'image
    src = cv2.imread("pic2.png")
    if src is None:
        print("Erreur : Impossible de charger l'image !")
        return

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    hue, saturation, _ = cv2.split(hsv)

    # Modèle paramétrique (Gaussien)
    mean_skin = np.array([100, 150, 200], dtype=np.float64)  # Exemple : moyennes R, G, B
    cov_skin = np.array([[1000, 50, 30], [50, 800, 20], [30, 20, 600]], dtype=np.float64)
    cov_inv_skin = np.linalg.inv(cov_skin)

    # Modèle non-paramétrique (histogramme 2D)
    h_bins, s_bins = 32, 32
    hist_size = [h_bins, s_bins]
    h_range, s_range = [0, 180], [0, 255]
    ranges = [h_range, s_range]

    mask = cv2.inRange(hsv, (0, 50, 50), (20, 255, 255))  # Masque peau
    hs_planes = [hue, saturation]
    hist = cv2.calcHist(hs_planes, [0, 1], mask, hist_size, ranges)
    hist = cv2.normalize(hist, hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Rétroprojection de l'histogramme
    back_proj = cv2.calcBackProject(hs_planes, [0, 1], hist, ranges, scale=1)

    # Fusion des modèles
    skin_prob_map = np.zeros(src.shape[:2], dtype=np.float64)

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            # Modèle paramétrique
            color = src[y, x].astype(np.float64)
            parametric_prob = mahalanobis_probability(color, mean_skin, cov_inv_skin)

            # Modèle non-paramétrique
            hs_prob = back_proj[y, x] / 255.0  # Normaliser entre 0 et 1

            # Fusion (moyenne pondérée)
            combined_prob = 0.5 * parametric_prob + 0.5 * hs_prob
            skin_prob_map[y, x] = combined_prob

    # Seuil et masque final
    skin_mask = (skin_prob_map > 0.5).astype(np.uint8) * 255

    # Affichage des résultats
    cv2.imshow("Image Source", src)
    cv2.imshow("Masque Peau Combiné", skin_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()