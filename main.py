import cv2
import numpy as np
import time

# Capture the background first (without you in frame)
cap = cv2.VideoCapture(0)
time.sleep(2)  # Give some time to adjust the camera

# Capture multiple frames to average the background
for i in range(60):
    ret, temp = cap.read()
    if ret:
        background = temp if i == 0 else cv2.addWeighted(background, 0.5, temp, 0.5, 0)

# Flip the background (optional, for mirror effect)
background = np.flip(background, axis=1)

# Create a named window and maximize it
cv2.namedWindow('Invisibility Cloak', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Invisibility Cloak', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)  # Mirror effect

    # Convert frame from BGR to HSV (easier to detect colors)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for light green color
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create mask to detect light green cloth
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Refine the mask for smoother edges
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    mask = cv2.dilate(mask, np.ones((5,5), np.uint8), iterations=2)
    mask = cv2.GaussianBlur(mask, (7,7), 0)

    # Segment out the green color part
    mask_inverse = cv2.bitwise_not(mask)

    # Extract background where green cloth is
    res1 = cv2.bitwise_and(background, background, mask=mask)

    # Extract person where green cloth is not
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inverse)

    # Combine the two
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display
    cv2.imshow('Invisibility Cloak', final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
