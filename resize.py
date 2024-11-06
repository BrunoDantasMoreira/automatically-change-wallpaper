import cv2
import numpy as np

def resized(image):
    
  # Check if image is valid
  if not isinstance(image, np.ndarray):
      print(type(image))
      print("Error: Invalid image. Expected a numpy array.")
      return None

  # Check if image is loaded properly
  if image is None:
      print("Error: Image not loaded. Check the file path.")
      return None  # Return None if image is not loaded

  # Convert the image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply a binary threshold to make the black bars stand out
  _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

  # Find contours in the thresholded image
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Ensure contours were found
  if not contours:
      print("Error: No contours found.")
      return None  # Return None if no contours are found

  # Get the bounding rectangle of the largest contour
  x, y, w, h = cv2.boundingRect(contours[0])

  # Crop the image to the bounding rectangle
  cropped_image = r'C:\Users\Dell\Pictures\cropped_image.png'

  # Save or display the cropped image
  cv2.imwrite(cropped_image, image[y:y+h, x:x+w])
  return cropped_image
