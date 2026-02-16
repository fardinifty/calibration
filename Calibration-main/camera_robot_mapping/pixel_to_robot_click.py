import cv2
import numpy as np

# Homography matrix from your compute_homography.py
H = np.array([
    [ 3.13906045e-01,  4.59214504e-02,  1.17664009e+02],
    [-2.60329492e-03,  6.17787119e-01, -1.25708906e+02],
    [-6.75754769e-04,  1.21594080e-04,  1.00000000e+00]
])

# Load image
img = cv2.imread("images/calib_image.jpg")

if img is None:
    print("Image not found")
    exit()

# Convert pixel → robot function
def pixel_to_robot(u, v):

    p = np.array([u, v, 1], dtype=np.float32).reshape(3,1)

    pr = H @ p

    pr = pr / pr[2,0]

    X = pr[0,0]
    Y = pr[1,0]

    return X, Y


# Mouse click event
def click_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        X, Y = pixel_to_robot(x,y)

        # Draw point
        cv2.circle(img, (x,y), 5, (0,0,255), -1)

        # Show pixel → robot mapping
        text = f"{x},{y} -> {X:.1f},{Y:.1f}"

        cv2.putText(img, text,
                    (x+10,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255,0,0),
                    2)

        print(f"Pixel ({x},{y}) -> Robot ({X:.2f},{Y:.2f})")


cv2.namedWindow("Mapping")
cv2.setMouseCallback("Mapping", click_event)

while True:

    cv2.imshow("Mapping", img)

    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cv2.destroyAllWindows()
