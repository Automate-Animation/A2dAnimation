import cv2
import numpy as np


def changing_color_using_hsv(
    img, color=[34, 0, 100], lower_hsv_value=[0, 0, 78], upper_hsv_value=[255, 255, 208]
):
    # extract alpha channel
    alpha = img[:, :, 3]

    # extract bgr channels
    bgr = img[:, :, 0:3]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, tuple(lower_hsv_value), tuple(upper_hsv_value))

    # change the image to make it green where the mask is white
    bgr_new = bgr.copy()
    bgr_new[mask == 255] = color

    # put alpha back into rgb_new
    bgra = cv2.cvtColor(bgr_new, cv2.COLOR_BGR2BGRA)
    bgra[:, :, 3] = alpha

    return bgra


## how to use this function:
# img = cv2.imread('eyes2.png', cv2.IMREAD_UNCHANGED)
# color_change_image=changing_color_using_hsv(img)
# cv2.imwrite('sword_masked_green.png', color_change_image)
