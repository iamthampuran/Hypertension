import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the fundus image
img = cv2.imread('./../ODIR-5K/ODIR-5K/Training Images/14_right.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to segment the image
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Apply morphological transformations to remove small objects and fill holes
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

# Find contours in the processed image
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
img_contours = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

opening = cv2.cvtColor(opening, cv2.COLOR_GRAY2BGR)

# Display the original image and the processed image
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(opening, cmap='gray'), plt.title('Processed Image')
plt.xticks([]), plt.yticks([])
plt.show()



cv2.imshow('Processed Image', cv2.resize(opening,(800,600)))
cv2.waitKey(0)
cv2.destroyAllWindows()
