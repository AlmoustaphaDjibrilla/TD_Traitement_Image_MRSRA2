import cv2

# Variables globales pour la ROI
Nline, Ncol = 80, 80
pas_yzoom, pas_xzoom = 10, 10
roi = None

# Callback pour gérer les événements de la souris
def cb_on_mouse(event, x, y, flags, param):
    global src, Nline, Ncol, roi

    if event == cv2.EVENT_RBUTTONDOWN:  # Zoom arrière
        Ncol += pas_xzoom
        Nline += pas_yzoom
    elif event == cv2.EVENT_LBUTTONDOWN:  # Zoom avant
        Ncol -= pas_xzoom
        Nline -= pas_yzoom

    # Définir la région d'intérêt
    x_start = max(x - Ncol // 2, 0)
    y_start = max(y - Nline // 2, 0)
    x_end = min(x_start + Ncol, src.shape[1])
    y_end = min(y_start + Nline, src.shape[0])
    roi = src[y_start:y_end, x_start:x_end]

    # Afficher la région d'intérêt
    if roi is not None:
        cv2.imshow("zoom", roi)

# Charger une image en niveaux de gris
src = cv2.imread("stuff.jpg", 0)

# Créer une fenêtre et associer le callback souris
cv2.namedWindow("stuff")
cv2.setMouseCallback("stuff", cb_on_mouse)

# Afficher l'image source
cv2.imshow("stuff", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
