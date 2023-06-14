import image_dehazer										# Load the library
import cv2
HazeImg = cv2.imread('images.jpg')						# read input image -- (**must be a color image**)
_ ,HazeCorrectedImg = image_dehazer.remove_haze(HazeImg)

#cv2.imshow('input image', HazeImg)				# display the original hazy image
cv2.imwrite('unhaze3.jpg', _)
#cv2.waitKey(0)