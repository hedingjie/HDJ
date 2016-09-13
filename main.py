# -*- coding: UTF-8 -*-
from SimpleCV import Camera,Display,Image,Color
import cv2
import numpy as np
import time
#---------------------函数-----------------
#确定圆心
def get_center(img):
    temp=img
    for i in range(5):
        temp=temp.erode()
    temp.save('target2.jpg')
    blobs=temp.findBlobs().sortArea()
    center=blobs[0]
    #print 'center:',center.coordinates()
    return center.coordinates()
#对图像进行二值化操作
def get_imgBin(img):
    img.binarize()
    temp=img.binarize().invert().morphOpen()
    return temp
#处理图像畸变 此处未实现
def emendation(img):
    return img
#获取环值
def get_score(point):
    #print point
    x_value=point[0]
    y_value=point[1]
    distance=np.sqrt((x_value-center[0])**2+(y_value-center[1])**2)
    score=0
    if distance<=102.83:
        score=10
    elif distance<=206.04:
        score=9
    elif distance<=308.42:
        score=8
    elif distance<=412.31:
        score=7
    elif distance<=513.28:
        score=6
    else:		#因为能读出的点位，表明都在有效区域，所以只考虑有效部分
        score=5
    return score
#------------------------------------------
img0=Image('demo.jpg')
disp=Display()
imgBin0=get_imgBin(img0)
imgBin0=emendation(imgBin0)   #图像校正
center=get_center(imgBin0)
img_list=[]
score=[]        #记录环值
templet=imgBin0
for i in range(1,11):
    img=Image('demo'+str(i)+'.jpg')
    img.save(disp)
    time.sleep(1)
    imgBin=get_imgBin(img)
    imgBin=emendation(imgBin)
    imgBin.save(disp)
    time.sleep(1)
    silhouette=(imgBin-templet).morphOpen()
    silhouette.save('target'+str(i)+'.jpg')
    blobs=silhouette.findBlobs()
    if(len(blobs)>0):
        point=blobs.sortArea()[-1].coordinates()
        score.append(get_score(point))
    templet=imgBin      #迭代处理
print 'CENTER',center,'\n环值如下：'
for i in range(len(score)):
    print score[i]
print '程序运行完毕！'


