import base64
import json
import os
import os.path as osp

import imgviz
import PIL.Image

from labelme.logger import logger
from labelme import utils

imgPath = './Json/'
allFileList = os.listdir(imgPath)

maskPath='./PedMasks/'
visualPath='./VISUAL/'

for file in allFileList:
    #file=DSCN0007.json
    if file==".DS_Store":
        continue

    #print(file)
    file_name = file[:len(file) - 5]
    print(file_name)

    json_file = imgPath+file_name+".json"

    if not osp.exists(maskPath):
        os.mkdir(maskPath)

    if not osp.exists(visualPath):
        os.mkdir(visualPath)

    data = json.load(open(json_file))
    imageData = data.get("imageData")

    if not imageData:
        imagePath = os.path.join(os.path.dirname(json_file), data["imagePath"])
        with open(imagePath, "rb") as f:
            imageData = f.read()
            imageData = base64.b64encode(imageData).decode("utf-8")
    img = utils.img_b64_to_arr(imageData)

    label_name_to_value = {"_background_": 0,"danger": 1,"safe": 2}
    for shape in sorted(data["shapes"], key=lambda x: x["label"]):
        label_name = shape["label"]
        if label_name in label_name_to_value:
            label_value = label_name_to_value[label_name]
        else:
            label_value = len(label_name_to_value)
            label_name_to_value[label_name] = label_value
    lbl, _ = utils.shapes_to_label(
        img.shape, data["shapes"], label_name_to_value
    )

    label_names = [None] * (max(label_name_to_value.values()) + 1)
    for name, value in label_name_to_value.items():
        label_names[value] = name

    
    lbl_viz = imgviz.label2rgb(
        label=lbl, img=imgviz.asgray(img), label_names=label_names, loc="rb"
    )

    utils.lblsave(osp.join(maskPath, file_name+".png"), lbl)
    PIL.Image.fromarray(lbl_viz).save(osp.join(visualPath, file_name+"_visual.png"))


    #logger.info("Saved to: {}".format(out_dir))






# Namespace(json_file='DSCN0009.json', out='DSCN0009_json')
