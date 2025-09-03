import cv2
import cvzone
import cvzone.FPS
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480) 
segmentor=SelfiSegmentation()
imgBg=cv2.imread("D:\Study\4th Sem\project\image\im.jpg")

listImg=os.listdir("image")
imgList=[]
for imgPath in listImg:
    img=cv2.imread(f'image/{imgPath}')
    imgList.append(img)
print(len(imgList))    

indexImg=0

while True:
    success,img=cap.read()
    imgOut=segmentor.removeBG(img,imgList[indexImg],cutThreshold=0.8)
    

    imgstacked=cvzone.stackImages([img,imgOut],2,1)

    cv2.imshow("Image Out",imgstacked)
    key=cv2.waitKey(1)
    if key==ord('a'):
        if indexImg>0:
            indexImg-=1
    elif key==ord('d'):
        if indexImg<len(imgList)-1:
            indexImg+=1
    elif key==ord('q'):
        break

    