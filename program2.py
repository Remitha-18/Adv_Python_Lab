import cv2
import numpy as np

img = np.zeros((500, 400, 3), dtype=np.uint8)

img[0:50, :] = (0, 30, 0)       # Very Dark Green
img[50:100, :] = (0, 50, 0)     # Dark Green
img[100:150, :] = (34, 139, 34) # Forest Green
img[150:200, :] = (0, 100, 0)   # Medium Green
img[200:250, :] = (0, 128, 0)   # Normal Green
img[250:300, :] = (50, 205, 50) # Lime Green
img[300:350, :] = (144, 238, 144) # Light Green
img[350:400, :] = (0, 255, 0)   # Bright Green
img[400:450, :] = (152, 251, 152) # Pale Green
img[450:500, :] = (170, 255, 195) # Mint Green

cv2.imshow("Green Shades", img)
cv2.waitKey(0)
cv2.destroyAllWindows()