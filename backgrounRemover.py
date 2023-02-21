import cv2
import numpy as np
import urllib.request

# Load the image
url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs8CMnDQDiWN83_CyovOzhbND3IPW-Jurrmg&usqp=CAU'
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on a white background
mask = np.zeros_like(img)
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=-1)

# Apply the mask to the original image
result = np.zeros_like(img)
result[mask == 255] = img[mask == 255]

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
