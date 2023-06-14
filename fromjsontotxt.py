import json


classes = ['ambulance', 'bicycle', 'bus', 'car', 'motorbike', 'pickup', 'truck', 'van', 'license']


# box form[x,y,w,h]
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) * dw / 2
    y = (box[1] + box[3]) * dh / 2
    w = (box[2] - box[0]) * dw
    h = (box[3] - box[1]) * dh
    return (x, y, w, h)


def convert_annotation():
    with open('labels.json', 'r') as f:
        datas = json.load(f)
        data = datas["annotations"]
        width = 1920
        height = 1080
    for item1 in data:
        file_name = item1["file_name"]
        objects = item1["objects"]
        outfile = open(r'C:\Users\vczyp\PycharmProjects\pythonProject\Vehicle\train\labels\*.txt' % (file_name[:-4]), 'a+')
        for item2 in objects:
            cls = item2["class"]
            cls_id = classes.index(cls)
            box = item2["position"]
            bb = convert((width, height), box)
            outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        outfile.close()


if __name__ == '__main__':
    convert_annotation()