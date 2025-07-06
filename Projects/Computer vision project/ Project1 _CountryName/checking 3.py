def create_overlay_image(polygons, warped_point, imgOverlay):
    """
    Create an overlay image with marked polygons based on the warped finger location.

    Parameters:
    - polygons: List of polygons representing countries.
    - warped_point: Coordinates of the index finger tip in the warped image.
    - imgOverlay: Overlay image to be marked.

    Returns:
    - imgOverlay: Overlay image with marked polygons.
    """
    # loop through all the countries
    #for polygon, name in polygons:
        #polygon_np = np.array(polygon, np.int32).reshape((-1, 1, 2))
        #result = cv2.pointPolygonTest(polygon_np, warped_point, False)
    for polygon, name in polygons:

        polygon_np = np.array(polygon, np.int32).reshape((-1, 1, 2))
        result = cv2.pointPolygonTest(polygon_np, warped_point, False)
        print(f"Testing {name}: result = {result}, point = {warped_point}")
        if result >= 0:
            cv2.polylines(imgOverlay, [np.array(polygon)], isClosed=True, color=(0, 255, 0), thickness=2)
            cv2.fillPoly(imgOverlay, [np.array(polygon)], (0, 255, 0))
            cvzone.putTextRect(imgOverlay, name, polygon[0], scale=1, thickness=1)
            cvzone.putTextRect(imgOverlay, name, (0, 100), scale=8, thickness=5)


    return imgOverlay





# Import necessary libraries
import pickle  # Pickle library for serializing Python objects
import cv2  # OpenCV library for computer vision tasks
import cvzone
import numpy as np  # NumPy library for numerical operations
from cvzone.HandTrackingModule import HandDetector

map_file_path = "D:\OPEN_CV Projects\INTRACTIVE MAP PROJECT\Step 1 – Get Corner Points\map.p"
countries_file_path = "D:\OPEN_CV Projects\INTRACTIVE MAP PROJECT\Step 2 – Create Country Polygons\countries.p"
cam_id = 0
width, height = 1280, 720

# Open a connection to the webcam
cap = cv2.VideoCapture(cam_id)  # For Webcam
# Set the width and height of the webcam frame
cap.set(3, width)
cap.set(4, height)

file_obj = open(map_file_path, 'rb')
map_points = pickle.load(file_obj)
# ✅ Load polygons (country shapes and names)
file_obj.close()
print(f"Loaded map coordinates.", map_points)

with open(countries_file_path, 'rb') as f:
    polygons = pickle.load(f)  # This should be a list of (points, country_name)


# Temporary list to store the four points of the current polygon being marked
current_polygon = []

# Counter to keep track of how many polygons have been created
counter = 0

detector = HandDetector(staticMode=False,
                        maxHands=1,
                        modelComplexity=1,
                        detectionCon=0.5,
                        minTrackCon=0.5)


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


def warp_single_point(point, matrix):
    """
    Warp a single point using the provided perspective transformation matrix.

    Parameters:
    - point: Coordinates of the point to be warped.
    - matrix: Perspective transformation matrix.

    Returns:
    - point_warped: Warped coordinates of the point.
    """
    # Convert the point to homogeneous coordinates
    point_homogeneous = np.array([[point[0], point[1], 1]], dtype=np.float32)

    # Apply the perspective transformation to the point
    point_homogeneous_transformed = np.dot(matrix, point_homogeneous.T).T

    # Convert back to non-homogeneous coordinates
    point_warped = point_homogeneous_transformed[0, :2] / point_homogeneous_transformed[0, 2]

    return point_warped


def warp_polygon(polygon, matrix):
    """
    Warp all the points in a polygon using the perspective transformation matrix.

    Parameters:
    - polygon: List of (x, y) points.
    - matrix: Perspective matrix from warp_image.

    Returns:
    - warped_polygon: List of transformed (x, y) points.
    """
    warped = []
    for pt in polygon:
        warped_pt = warp_single_point(pt, matrix)
        warped.append((int(warped_pt[0]), int(warped_pt[1])))
    return warped



def get_finger_location(img, imgWarped):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        indexFinger = hand1["lmList"][8][0:2]  # List of 21 landmarks for the first hand
        #cv2.circle(img,indexFinger,5,(255,0,255),cv2.FILLED)
        warped_point = warp_single_point(indexFinger, matrix)
        warped_point = int(warped_point[0]), int(warped_point[1])
        print(indexFinger,warped_point)
        cv2.circle(imgWarped, warped_point, 5, (255, 0, 0), cv2.FILLED)
    else:
        warped_point = None

    return warped_point


def create_overlay_image(polygons, warped_point, imgOverlay):
    """
    Create an overlay image with marked polygons based on the warped finger location.

    Parameters:
    - polygons: List of polygons representing countries.
    - warped_point: Coordinates of the index finger tip in the warped image.
    - imgOverlay: Overlay image to be marked.

    Returns:
    - imgOverlay: Overlay image with marked polygons and debug visuals.
    """
    for polygon, name in polygons:
        polygon_np = np.array(polygon, np.int32).reshape((-1, 1, 2))

        # 🔍 Visualize the polygon
        cv2.polylines(imgOverlay, [np.array(polygon)], isClosed=True, color=(0, 255, 255), thickness=2)

        # 🔍 Visualize the finger point
        if warped_point is not None:
            cv2.circle(imgOverlay, warped_point, 6, (0, 0, 255), -1)

        # ➕ Debug info
        result = cv2.pointPolygonTest(polygon_np, warped_point, False)
        print(f"Testing {name}: result = {result}, point = {warped_point}, polygon = {polygon}")

        # ✅ Finger is inside this polygon
        if result >= 0:
            cv2.fillPoly(imgOverlay, [np.array(polygon)], (0, 255, 0))
            cvzone.putTextRect(imgOverlay, name, polygon[0], scale=1, thickness=1)
            cvzone.putTextRect(imgOverlay, name, (50, 100), scale=5, thickness=5, offset=10, colorT=(255, 255, 255), colorR=(0, 150, 0))

    return imgOverlay




def inverse_warp_image(img, imgOverlay, map_points):
    """
    Inverse warp an overlay image onto the original image using provided map points.

    Parameters:
    - img: Original image.
    - imgOverlay: Overlay image to be warped.
    - map_points: List of four points representing the region on the map.

    Returns:
    - result: Combined image with the overlay applied.
    """
    # Convert map_points to NumPy array
    map_points = np.array(map_points, dtype=np.float32)

    # Define the destination points for the overlay image
    destination_points = np.array([[0, 0], [imgOverlay.shape[1] - 1, 0], [0, imgOverlay.shape[0] - 1],
                                   [imgOverlay.shape[1] - 1, imgOverlay.shape[0] - 1]], dtype=np.float32)

    # Calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(destination_points, map_points)

    # Warp the overlay image to fit the perspective of the original image
    warped_overlay = cv2.warpPerspective(imgOverlay, M, (img.shape[1], img.shape[0]))

    # Combine the original image with the warped overlay
    result = cv2.addWeighted(img, 1, warped_overlay, 0.65, 0, warped_overlay)

    return result






while True:
    success, img = cap.read()
    imgWarped, matrix = warp_image(img, map_points)
    imgOutput = img.copy()
    #imgOverlay = imgWarped.copy()  # <-- Make sure this is defined
    # Find the hand and its landmarks
    #warped_point = get_finger_location(imgWarped)
    warped_point = get_finger_location(img, imgWarped)
    h, w, _ = imgWarped.shape
    imgOverlay = np.zeros((h, w, 3), dtype=np.uint8)

    #if warped_point:
        #imgOverlay = create_overlay_image(polygons, warped_point, imgOverlay)
        #imgOutput = inverse_warp_image(img, imgOverlay, map_points)

    if warped_point:
        # Warp all country polygons once using the current transformation matrix
        polygons_warped = [(warp_polygon(polygon, matrix), name) for polygon, name in polygons]

        # Use the warped polygons to draw overlay and detect finger position
        imgOverlay = create_overlay_image(polygons_warped, warped_point, imgOverlay)

        # Warp overlay back to original image perspective
        imgOutput = inverse_warp_image(img, imgOverlay, map_points)

    # Stack all images (2 rows, scale = 0.3)
    #imgStacked = cvzone.stackImages([img, imgWarped, imgOutput, imgOverlay], 2, 0.3)
    #cv2.imshow("Stacked Image", imgStacked)
    # cv2.imshow("Original Image", img)
    cv2.imshow("Warped Image", imgWarped)
    cv2.imshow("Output Image", imgOutput)
    key = cv2.waitKey(1)
