from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
  i= image.open(path)
  image_array = np.array(i)
    

from scipy.signal import convolve2d # Import the convolve2d function

def edge_detection(image_array):
  gray_image = np.mean(image_array, axis=2)

  y_filter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
  x_filter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
  
  # Apply the filters using convolve2d
  edgeX = convolve2d(gray_image, x_filter, mode='same', boundary='symm')  
  edgeY = convolve2d(gray_image, y_filter, mode='same', boundary='symm')  
  
  edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
  return edgeMAG
