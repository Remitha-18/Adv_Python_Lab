import cv2

# Create a blank white image
img = 255 * (cv2.UMat(500, 700, cv2.CV_8UC3).get())

drawing = False
start_x, start_y = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_x, start_y, img

    # When left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    # When mouse button is released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (start_x, start_y), (x, y), (255, 0, 0), 2)

# Create window
cv2.namedWindow("Draw Rectangle")

# Connect mouse with function
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

while True:
    cv2.imshow("Draw Rectangle", img)

    key = cv2.waitKey(1)

    # Press ESC to exit
    if key == 27:
        break

cv2.destroyAllWindows()