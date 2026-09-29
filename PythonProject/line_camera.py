import cv2

cap = cv2.VideoCapture(0)

points = []


def draw_line(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags == cv2.EVENT_FLAG_LBUTTON:
            points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))


cv2.namedWindow("Line Camera")
cv2.setMouseCallback("Line Camera", draw_line)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Cannot access camera")
        break

    # Draw red lines
    for i in range(1, len(points)):
        cv2.line(
            frame,
            points[i - 1],
            points[i],
            (0, 0, 255),
            5
        )

    cv2.imshow("Line Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    # C = clear lines
    if key == ord('c'):
        points.clear()

    # Q = quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()