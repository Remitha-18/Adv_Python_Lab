import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Kernel for removing noise
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot access webcam")
        break

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ---------------- RED ----------------
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = red_mask1 + red_mask2

    # ---------------- GREEN ----------------
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([90, 255, 255])

    green_mask = cv2.inRange(
        hsv,
        lower_green,
        upper_green
    )

    # ---------------- BLUE ----------------
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    blue_mask = cv2.inRange(
        hsv,
        lower_blue,
        upper_blue
    )

    # ---------------- YELLOW ----------------
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([35, 255, 255])

    yellow_mask = cv2.inRange(
        hsv,
        lower_yellow,
        upper_yellow
    )

    # ---------------- PINK ----------------
    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])

    pink_mask = cv2.inRange(
        hsv,
        lower_pink,
        upper_pink
    )

    # Dictionary containing colors and their masks
    colors = {
        "Red": (red_mask, (0, 0, 255)),
        "Green": (green_mask, (0, 255, 0)),
        "Blue": (blue_mask, (255, 0, 0)),
        "Yellow": (yellow_mask, (0, 255, 255)),
        "Pink": (pink_mask, (180, 105, 255))
    }

    # Detect each color
    for color_name, (mask, box_color) in colors.items():

        # Remove small noise
        mask = cv2.erode(mask, kernel)
        mask = cv2.dilate(mask, kernel)

        # Find contours
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Process each contour
        for contour in contours:

            area = cv2.contourArea(contour)

            # Ignore very small objects
            if area > 1000:

                x, y, w, h = cv2.boundingRect(contour)

                # Draw rectangle
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    box_color,
                    2
                )

                # Display color name
                cv2.putText(
                    frame,
                    color_name,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    box_color,
                    2
                )

    # Show result
    cv2.imshow("Color Detection", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()