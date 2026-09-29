import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access camera")
    exit()

flip = False

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read camera")
        break

    # Press 1 to flip
    if flip:
        frame = cv2.flip(frame, 1)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        flip = not flip

    # Press q to quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()