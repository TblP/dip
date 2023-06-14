import os
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imgaug.augmenters as iaa
import glob

image = []
image_path = glob.glob(r'C:\Users\vczyp\PycharmProjects\pythonProject\data\*.jpg')

for img_ in image_path:
    img = cv2.imread(img_)
    print(len(image))
    image.append(img)

seq = iaa.Sequential([
            iaa.PerspectiveTransform(random_state=1, scale=0.05),
            iaa.Fog(seed=random.randint(0, 9)),
            iaa.Affine(rotate=0.01),
            iaa.GammaContrast(3)
        ])

print('start seq')
au = []
for im in range(len(image)):
    print(im)
    au.append(seq(image=image[im]))

path = r'C:\Users\vczyp\PycharmProjects\pythonProject\save'

print('start save')
for img in range(len(au)):
    cv2.imwrite(os.path.join(path, str(img)+'.jpg'), au[img])