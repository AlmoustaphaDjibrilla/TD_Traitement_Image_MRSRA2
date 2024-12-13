import cv2
import numpy as np
import math

# Dimensions de l'image
width = 628
height = 100

# Créer une image blanche
graph_img = np.full((height, width), 255, dtype=np.uint8)

# Calcul et traçage des points
for k in range(0, width, 4):
    x = k
    y = round(50 * (1 - math.cos(x / 100.)))
    cv2.circle(graph_img, (x, y), 1, (0, 0, 0), -1)

# Afficher le graphe
cv2.imshow("Graph", graph_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
