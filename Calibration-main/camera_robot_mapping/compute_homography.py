import numpy as np
import cv2

img_pts = np.array([
    [433,205],
    [218,355],
    [226,250],
    [283,147],
    [437,101],
    [538,155],
    [591,314],
    [652,105]
], dtype=np.float32)

robot_pts = np.array([
    [350,0],
    [225,100],
    [225,50],
    [275,-50],
    [350,-100],
    [450,-50],
    [500,100],
    [575,-100]
], dtype=np.float32)

H, mask = cv2.findHomography(img_pts, robot_pts)

print("Homography matrix:")
print(H)
