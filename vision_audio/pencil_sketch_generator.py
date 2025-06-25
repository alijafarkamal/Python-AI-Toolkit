import cv2
import numpy as np
def pencil_sketch(img_path,output_path):
    # Read the image
    img = cv2.imread(img_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Invert the image
    inverted_gray_image = 255 - gray_image
    # Blur the image by using the Gaussian Function
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    # Invert the blurred image
    inverted_blurred_img = 255 - blurred_img
    # Create the pencil sketch image
    pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
    # Save the pencil sketch image
    cv2.imwrite(output_path, pencil_sketch_img)
    cv2.imshow("pencil sketch", pencil_sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# Call the function
pencil_sketch("ali.jpg", "pencil_sketch.jpg")