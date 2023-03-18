import numpy as np
import os
import cv2

imgPath = './PedMasks/'
newPath='./Black/'

allFileList = os.listdir(imgPath)


for file in allFileList:
    if file==".DS_Store":
        continue
    file_name = file
    print(file)
    file1 = imgPath+file_name
    file2 =newPath+file_name
    img = cv2.imread(file1)

    b=img[:,:,1]==128
    s=2*b.astype(int)
    c=img[:,:,2]==128
    s+=c.astype(int)
    dd=np.dstack((s,s,s))

    cv2.imwrite(file2, dd)

