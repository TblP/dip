import torchattacks
import cv2
import torch
import os
from torchvision import transforms
from PIL import Image

images = r'C:\Users\vczyp\PycharmProjects\pythonProject\test2_2.jpg'
img = Image.open(images)
convert_tensor = transforms.ToTensor()
img = convert_tensor(img)
path_model = r'C:\Users\vczyp\PycharmProjects\pythonProject\yolov7\runs\train\yolov74\weights\last.pt'
labels = ['ambulance', 'bicycle', 'bus', 'car', 'motorbike', 'pickup', 'truck', 'van', 'license']
n_classses = 9

model = torch.hub.load("WongKinYiu/yolov7", 'custom', path_model, trust_repo=True)
labels = torch.Tensor(n_classses)

atk = torchattacks.PGD(model, eps=8/255, alpha=2/255, steps=4)

atk.set_mode_targeted_by_label(quiet=True)
# do not show the message
# shift all class loops one to the right, 1=>2, 2=>3, .., 9=>0
target_labels = (labels + 1) % 10


adv_images = atk(img, target_labels)

cv2.imshow('adv', adv_images)
cv2.waitkey(0)