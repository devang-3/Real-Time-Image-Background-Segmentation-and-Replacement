indexImg=0

# while True:
#     success,img=cap.read()
#     imgOut=segmentor.removeBG(img,imgList[indexImg],cutThreshold=0.8)
    

#     imgstacked=cvzone.stackImages([img,imgOut],2,1)
# #    _, imgstacked=fpsReader.update(imgstacked,color=(0,0,255))
#     print(indexImg)

#     cv2.imshow("Image Out",imgstacked)
#     key=cv2.waitKey(1)
#     if key==ord('a'):
#         if indexImg>0:
#             indexImg-=1
#     elif key==ord('d'):
#         if indexImg<len(imgList)-1:
#             indexImg+=1
#     elif key==ord('q'):
#         break

    