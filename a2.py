import cv2
import os
import numpy as np

# Define paths
VIDEO_NAME = "fingers"
FVideo = f'videos/{VIDEO_NAME}.mp4'
WORKDIR = f"videos/{VIDEO_NAME}/"
os.makedirs(WORKDIR, exist_ok=True)
FFirst = WORKDIR + "first.png"  # Filename for the first frame image

# Create video capture object
vidCap = cv2.VideoCapture(FVideo)

# Read the first frame
success, image = vidCap.read()
if success:
    cv2.imwrite(FFirst, image)  # Save the first frame image
    # Here insert the code for hand detection
    # As an example, let's assume we use a simple color-based detection
    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define the range of skin color in HSV
    lower_skin = np.array([0, 48, 80], dtype="uint8")
    upper_skin = np.array([20, 255, 255], dtype="uint8")
    # Create a mask based on the defined color range
    skinMask = cv2.inRange(hsv, lower_skin, upper_skin)
    # Apply the mask to the image
    skin = cv2.bitwise_and(image, image, mask=skinMask)
    # Show the result
    cv2.imshow("Skin detection", skin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to read the video")

vidCap.release()
