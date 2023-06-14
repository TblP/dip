import os
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imgaug.augmenters as iaa
import glob

image = []

image_path = r'C:\Users\vczyp\PycharmProjects\pythonProject\labels'

count = 0
for file_name in os.listdir(image_path):

    # Construct old file name
    source = os.path.join(image_path, file_name)

    # Adding the count to the new file name and extension
    destination = os.path.join(r'C:\Users\vczyp\PycharmProjects\pythonProject\labels2', str(count) + ".txt")

    # Renaming the file
    os.rename(source, destination)
    count += 1