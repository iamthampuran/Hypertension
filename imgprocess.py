import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_hypertension(image_path):
    # Load the image and convert it to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median filtering to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Segment the blood vessels using Otsu's method
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Calculate the width of the blood vessels
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(thresh,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    edges = cv2.Canny(dilation,50,150)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

    # If lines are detected, calculate the average width of the blood vessels
    if lines is not None:
        total_width = 0
        count = 0
        for line in lines:
            x1, y1, x2, y2 = line[0]
            width = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            total_width += width
            count += 1
        avg_width = total_width / count

        # Determine if the image has hypertension or not
        if avg_width > 10:
            print("The fundus image has hypertension")
        else:
            print("The fundus image does not have hypertension")
    else:
        print("No blood vessels were detected")

    # Display the processed image
    plt.imshow(edges, cmap='gray')
    plt.show()

image_path = "../ODIR-5K/ODIR-5K/Training Images/127_left.jpg"
detect_hypertension(image_path)
