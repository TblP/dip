import numpy as np

import cv2

from matplotlib import pyplot as plt

image = cv2.imread(r'C:\Users\vczyp\PycharmProjects\pythonProject\unhaze.jpg',1)

image_bw = cv2.imread(r'C:\Users\vczyp\PycharmProjects\pythonProject\unhaze.jpg',0)

noiseless_image_bw = cv2.fastNlMeansDenoising(image_bw, None, 20, 7, 21)

noiseless_image_colored = cv2.fastNlMeansDenoisingColored(image,None,20,20,7,21)

titles = ['Original Image(colored)','Image after removing the noise (colored)', 'Original Image (grayscale)','Image after removing the noise (grayscale)']
images = [image,noiseless_image_colored, image_bw, noiseless_image_bw]
plt.figure(figsize=(13,5))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()