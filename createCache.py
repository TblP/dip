import os
import torch
import numpy as np
dic = {}
path = r'C:\Users\vczyp\PycharmProjects\pythonProject\vehicleNoise\train\labels'
for i in os.listdir(path):
    with open(os.path.join(path, i)) as annotation:
        p = []
        for j in annotation.readlines():
            arr = list(map(float,j.strip().split()))
            p.append(arr)
    dic[fr'C:\Users\vczyp\PycharmProjects\pythonProject\vehicleNoise\train\images\{i}'] = [np.array(p, dtype=float), (800, 600)]

torch.save(dic,'labels.cache')