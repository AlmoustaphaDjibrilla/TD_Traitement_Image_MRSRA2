import cv2
def on_mouse_zoom_img(event, x, y, flags, param):
    global src, roi

    if roi is not None and event == cv2.EVENT_MOUSEMOVE:
        abs_x = roi['x'] + x
        abs_y = roi['y'] + y
        if 0 <= abs_x < src.shape[1] and 0 <= abs_y < src.shape[0]:
            intensity = src[abs_y, abs_x]
            cv2.setTrackbarPos("Grey Level", "zoom", intensity)

# Ajout du curseur et du callback dans la fenêtre zoom
cv2.namedWindow("zoom")
cv2.createTrackbar("Grey Level", "zoom", 0, 255, lambda x: None)
cv2.setMouseCallback("zoom", on_mouse_zoom_img)
