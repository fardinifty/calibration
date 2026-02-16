import cv2

points_img = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked pixel: ({x}, {y})")
        points_img.append((x, y))

img = cv2.imread("images/calib_image.jpg")
if img is None:
    print("Image not found")
    exit()

cv2.namedWindow("calib")
cv2.setMouseCallback("calib", click_event)

while True:
    cv2.imshow("calib", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        break

cv2.destroyAllWindows()
print("Collected pixel points:", points_img)
