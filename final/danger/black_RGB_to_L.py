import numpy as np
import os
from PIL import Image



imgPath = './Black/'
newPath='./Black_L/'

allFileList = os.listdir(imgPath)


for file in allFileList:
    if file==".DS_Store":
        continue
    file_name = file
    print(file)
    file1 = imgPath+file_name
    file2 =newPath+file_name
    img = Image.open(file1)
    img=img.convert("L")


    img.save(file2)

