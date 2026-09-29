import cv2 as cv

# Open the webcam
cap = cv.VideoCapture(0)

# Create Background Subtractor
back_sub = cv.createBackgroundSubtractorMOG2()

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot receive frame")
        break

    # Apply background subtraction
    mask = back_sub.apply(frame)

    # Remove shadows and noise
    _, mask = cv.threshold(mask, 200, 255, cv.THRESH_BINARY)

    # Find contours
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around moving objects
    for cnt in contours:

        # Ignore very small movements
        if cv.contourArea(cnt) < 1000:
            continue

        x, y, w, h = cv.boundingRect(cnt)

        # Draw rectangle
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display label
        cv.putText(frame, "Motion",
                   (x, y - 10),
                   cv.FONT_HERSHEY_SIMPLEX,
                   0.6,
                   (0, 255, 0),
                   2)

    # Show original frame
    cv.imshow("Motion Detection", frame)

    # Show motion mask
    cv.imshow("Foreground Mask", mask)

    # Press Q to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()