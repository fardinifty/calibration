import cv2

# Load image
img = cv2.imread("images/calib_image.jpg")

if img is None:
    print("Image not found")
    exit()

points_img = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points_img.append((x, y))

        # Draw a small circle
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        # Write pixel coordinates on image
        text = f"({x}, {y})"
        cv2.putText(
            img,
            text,
            (x + 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            1
        )

        print(f"Clicked at pixel: ({x}, {y})")

# Create window and set mouse callback
cv2.namedWindow("calibration")
cv2.setMouseCallback("calibration", click_event)

while True:
    cv2.imshow("calibration", img)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()

print("Collected points:")
print(points_img)
