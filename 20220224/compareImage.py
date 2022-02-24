import glob
import cv2
import numpy as np
from PIL import Image

#画像データをPillowとNumpyで取得
def main(img1, img2):
    target1 = cv2.cvtColor(np.array(Image.open(img1)), cv2.COLOR_BGR2GRAY)
    target2 = cv2.cvtColor(np.array((Image.open(img2)).resize((target1.shape[1],target1.shape[0]))), cv2.COLOR_BGR2GRAY)
    target1 = cv2.GaussianBlur(target1, (9,9), 1)
    target2 = cv2.GaussianBlur(target2, (9,9), 1)
    resultImage = cv2.absdiff(target1, target2)
    cv2.imshow("result", resultImage)
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
    print("一つ目の画像のパスを入力してください。imgPath1 ：")
    img1 = input()
    print("二つ目の画像のパスを入力してください。imgPath2 ：")
    img2 = input()
    main(img1, img2)


