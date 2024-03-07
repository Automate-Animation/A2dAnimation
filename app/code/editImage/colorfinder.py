import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("tracker")
cv2.createTrackbar("LH", "tracker", 0, 255, nothing)
cv2.createTrackbar("LS", "tracker", 0, 255, nothing)
cv2.createTrackbar("LV", "tracker", 0, 255, nothing)

cv2.createTrackbar("UH", "tracker", 255, 255, nothing)
cv2.createTrackbar("US", "tracker", 255, 255, nothing)
cv2.createTrackbar("UV", "tracker", 255, 255, nothing)


while True:
    frame = cv2.imread(
        "G:/Projects/speech aligner/kamal speech aliner/speach_aliner/app/frames/bodyFrames/398.png",
        1,
    )  # add image

    scale_percent = 20  # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    #     l_b=np.array([110,50,50])#lower bound
    #     u_b=np.array([130,250,250])#upper bound

    l_h = cv2.getTrackbarPos("LH", "tracker")
    l_s = cv2.getTrackbarPos("LS", "tracker")
    l_V = cv2.getTrackbarPos("LV", "tracker")

    u_h = cv2.getTrackbarPos("UH", "tracker")
    u_s = cv2.getTrackbarPos("US", "tracker")
    u_V = cv2.getTrackbarPos("UV", "tracker")

    l_b = np.array([l_h, l_s, l_V])  # lower bound
    u_b = np.array([u_h, u_s, u_V])  # upper  bound

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #     res[mask==255]=(0,0,255)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
print("l_b ", l_b)
print("u_b ", u_b)
