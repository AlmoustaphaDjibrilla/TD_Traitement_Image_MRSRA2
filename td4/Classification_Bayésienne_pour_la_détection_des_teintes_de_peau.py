import cv2
import numpy as np

def mahalanobis_distance(x, mean, cov_inv):
    """
    Calcule la distance de Mahalanobis.
    :param x: Vecteur à classifier (ex. une couleur).
    :param mean: Moyenne de la distribution.
    :param cov_inv: Inverse de la matrice de covariance.
    :return: Distance de Mahalanobis.
    """
    diff = x - mean
    dist = np.dot(np.dot(diff.T, cov_inv), diff)
    return dist

def is_skin_color(x, mean_skin, cov_inv_skin, threshold):
    """
    Vérifie si une couleur appartient à la classe peau en fonction d'un seuil.
    :param x: Couleur (vecteur).
    :param mean_skin: Moyenne de la distribution des couleurs peau.
    :param cov_inv_skin: Inverse de la matrice de covariance des couleurs peau.
    :param threshold: Seuil de classification.
    :return: True si la couleur est classée comme peau, False sinon.
    """
    dist = mahalanobis_distance(x, mean_skin, cov_inv_skin)
    return dist <= threshold

def main():
    # Exemple : Modèle Gaussien pour la peau
    mean_skin = np.array([100, 150, 200])  # Exemples de moyennes R, G, B
    cov_skin = np.array([[1000, 50, 30],
                         [50, 800, 20],
                         [30, 20, 600]])  # Exemple de matrice de covariance
    cov_inv_skin = np.linalg.inv(cov_skin)
    threshold = 3.0  # Seuil pour classifier comme "peau"

    # Charger une image et itérer sur ses pixels
    src = cv2.imread("pic2.png")
    if src is None:
        print("Erreur : Impossible de charger l'image !")
        return

    skin_mask = np.zeros(src.shape[:2], dtype=np.uint8)

    # Vérification des pixels
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            color = src[y, x].astype(np.float64)
            if is_skin_color(color, mean_skin, cov_inv_skin, threshold):
                skin_mask[y, x] = 255  # Marquer comme peau

    # Afficher le résultat
    cv2.imshow("Image Source", src)
    cv2.imshow("Masque Peau", skin_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
