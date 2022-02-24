from email.mime import base
import glob
import cv2
import numpy as np
from PIL import Image

#画像データをPillowとNumpyで取得
def main(img1, img2):
    baseImage = cv2.cvtColor(np.array(Image.open(img1)), cv2.COLOR_BGR2RGB)
    targetImage = cv2.cvtColor(np.array(Image.open(img2)), cv2.COLOR_BGR2RGB)
    h,w,c = targetImage.shape
    baseImagecopy = baseImage.copy()
    targetList=[]
    result = cv2.matchTemplate(baseImage, targetImage, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    while(maxVal>0.999):
        targetList.append(maxLoc)
        for i in range(h):
            for j in range(w):
                baseImage[maxLoc[1]+i][maxLoc[0]+j]=[0,0,0]
        #cv2.imshow("test",baseImage)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        result = cv2.matchTemplate(baseImage, targetImage, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    for i in targetList:
        for j in range(h):
            baseImagecopy[i[1]+j][i[0]]=[255,0,255]
            baseImagecopy[i[1]+j][i[0]-1]=[255,0,255]
            baseImagecopy[i[1]+j][i[0]+1]=[255,0,255]
            baseImagecopy[i[1]+j][i[0]+w]=[255,0,255]
            baseImagecopy[i[1]+j][i[0]-1+w]=[255,0,255]
            baseImagecopy[i[1]+j][i[0]+1+w]=[255,0,255]
        for j in range(w):
            baseImagecopy[i[1]][i[0]+j]=[255,0,255]
            baseImagecopy[i[1]-1][i[0]+j]=[255,0,255]
            baseImagecopy[i[1]+1][i[0]+j]=[255,0,255]
            baseImagecopy[i[1]+h][i[0]+j]=[255,0,255]
            baseImagecopy[i[1]-1+h][i[0]+j]=[255,0,255]
            baseImagecopy[i[1]+1+h][i[0]+j]=[255,0,255]

    cv2.imshow('resultimage', baseImagecopy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    #ファイル名取得(大文字も読み込んでくれるみたい)
    imageList = glob.glob("targetImages/*.png")
    imageList.extend(glob.glob("targetImages/*.jpg"))
    imageList.extend(glob.glob("targetImages/*.jpeg"))

    if(len(imageList)!=2):
        print("対象画像は2つのみにしてください")
        exit()
    main(imageList[0], imageList[1])
else:
    print("一つ目の画像のパスを入力してください。base ：")
    baseImage = input()
    print("二つ目の画像のパスを入力してください。target ：")
    targetImage = input()
    main(baseImage, targetImage)

