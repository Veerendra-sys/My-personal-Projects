1. Setup & Loading Data
python
Copy
Edit
import pickle, cv2, cvzone, numpy as np
from cvzone.HandTrackingModule import HandDetector
Imports necessary libraries

Loads:

map.p: 4 corner points of the map region

countries.p: list of saved country polygons with names

2. Initialize Webcam and Detector
python
Copy
Edit
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

detector = HandDetector(...)
Captures live video from webcam

Initializes hand tracking with up to 1 hand and medium detection confidence

3. Warping Image and Points
python
Copy
Edit
def warp_image(img, points, size)
def warp_single_point(point, matrix)
def warp_polygon(polygon, matrix)
These functions perform:

Perspective transformation of entire images

Warping of individual points or entire polygons using matrix math

4. Detecting Finger Location
python
Copy
Edit
def get_finger_location(img, imgWarped)
Detects hand

Extracts index finger tip (landmark 8)

Warps that point using the same transformation matrix to locate it in map space

5. Create Overlay Based on Finger Inside Polygon
python
Copy
Edit
def create_overlay_image(polygons, warped_point, imgOverlay)
Checks if finger is inside any country polygon using cv2.pointPolygonTest()

If true:

Draws filled green polygon

Adds country name using cvzone.putTextRect()

6. Warp Overlay Back to Original Image
python
Copy
Edit
def inverse_warp_image(img, imgOverlay, map_points)
Takes the warped overlay (highlighted regions)

Uses inverse transformation to map it back to original camera perspective

7. Main Loop
python
Copy
Edit
while True:
    img = camera feed
    imgWarped = warped map
    warped_point = finger position
    polygons_warped = all country shapes warped
    imgOverlay = marked polygons
    imgOutput = final result overlayed on original feed
Everything comes together in this loop:

Hand detection

Finger warping

Polygon detection

Inverse overlaying

🎯 Possible Interview Questions + Sample Answers
✅ Q1: What is perspective transformation? Why did you use it?
A:
Perspective transformation is a way to map a quadrilateral (like a tilted sheet or map) to a rectangle (top-down view). I used it to "flatten" the region of interest (map area) from the camera feed so I can reliably detect polygon regions and map interactions.

✅ Q2: How did you track the finger using OpenCV?
A:
I used the cvzone.HandTrackingModule which is built on MediaPipe. It detects 21 hand landmarks, and I specifically used landmark index 8 (tip of index finger) to track pointing actions. I then warped this point using the transformation matrix to check its position on the map.

✅ Q3: How do you detect whether a point is inside a polygon?
A:
I used cv2.pointPolygonTest(), which checks whether a point lies inside a given polygon (returns ≥ 0 if inside). This allows us to know which country (polygon) the finger is pointing to.

✅ Q4: What is inverse warping and why did you use it?
A:
Inverse warping is the process of mapping an overlay (like drawn polygons on a warped map) back onto the original camera feed. I used it so that the user sees the country names and highlights directly in the original view — not just in the warped map window.

✅ Q5: Why did you use cv2.addWeighted()?
A:
It allows blending two images with transparency. I used it to create a semi-transparent overlay so that the highlighted polygons can be shown on top of the base image without completely hiding it.
✅ Q6: What’s the role of pickle here?
A:
pickle is used to serialize and load Python objects — in this case:
map.p: 4 corner points of the map
countries.p: list of country polygons with names
It’s efficient and Pythonic for local data persistence.
📝 Resume/Portfolio Project Summary
Developed a real-time interactive map system using OpenCV, allowing users to point at a warped map with their finger and detect which country region (polygon) they're pointing to. The project includes live webcam feed processing, perspective transformation, hand tracking with MediaPipe, polygon detection, and overlay rendering with inverse mapping.