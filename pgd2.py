
import torch


path_model = r'/yolov56/runs/train/exp43/weights/last.pt'
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

model.eval()
