import pickle
import cv2
import numpy as np

#########################
# Camera settings
cam_id = 0 # ✅ Iriun camera index
width, height = 1280, 720 # ✅ Desired resolution
#########################

# Initialize camera
cap = cv2.VideoCapture(cam_id)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Check camera open status
if not cap.isOpened():
    print("❌ Camera not detected. Check if Iriun is running.")
    exit()

points = np.zeros((4, 2), int)
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN and counter < 4:
        points[counter] = x, y
        counter += 1
        print(f"✅ Point {counter} selected: ({x}, {y})")
def reorder_points(pts):
    """
    Reorders 4 corner points in the order:
    top-left, top-right, bottom-left, bottom-right.
    """
    pts = np.array(pts)
    reordered = np.zeros((4, 2), dtype=np.float32)

    s = pts.sum(axis=1)
    reordered[0] = pts[np.argmin(s)]      # Top-left
    reordered[3] = pts[np.argmax(s)]      # Bottom-right

    diff = np.diff(pts, axis=1)
    reordered[1] = pts[np.argmin(diff)]   # Top-right
    reordered[2] = pts[np.argmax(diff)]   # Bottom-left

    return reordered

def warp_image(img, points, size=[1280,720]):
    points = reorder_points(points)
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [size[0], 0], [0, size[1]], [size[0], size[1]]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (size[0], size[1]))
    return imgOutput, matrix


while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to read frame from camera.")
        break

    if counter == 4:
        # Save points to file only once
        with open("map.p", "wb") as fileObj:
            pickle.dump(points, fileObj)
        print("✅ Points saved to file: map.p")

        # Warp and show image
        imgOutput, matrix = warp_image(img, points)
        cv2.imshow("📐 Warped Output", imgOutput)

    # Draw selected points
    for x in range(counter):  # Draw only selected points
        cv2.circle(img, (points[x][0], points[x][1]), 5, (0, 255, 0), cv2.FILLED)

    cv2.imshow("📷 Iriun Live Feed", img)
    cv2.setMouseCallback("📷 Iriun Live Feed", mousePoints)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
