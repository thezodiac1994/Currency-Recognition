
# coding: utf-8

# In[100]:


############################################################################################
# Import Libraries
import numpy as np
import os
import glob
import re
import cv2
from scipy import misc
from random import randint

############################################################################################
# Create Synthetic Image
def createSyntheticImage():
    subFileList = []
    imageList = []
    modImageDirPath = []
    print("Creating Synthetic Data ...")
    pathToImage = os.path.realpath("Dataset")
    imgPath = os.path.join(pathToImage,'*')
    fileList = glob.glob(imgPath)
    for i in range(len(fileList)):
        subDirectoryPath = os.path.join(fileList[i],'*');
        subFileList.append(glob.glob(subDirectoryPath))
    subNpArray = np.array(subFileList)
    for i in range(len(subNpArray)):
        for j in range(len(subNpArray[i])):
            imageDirPath = os.path.join(subNpArray[i][j],'*.jpg')
            modImageDirPath.append(imageDirPath.replace("*.jpg",""))
            imageList.append(glob.glob(imageDirPath))
    print(len(imageList))
    for k in range(len(imageList)):
        for r in range(len(imageList[k])):
            imageAugmentation(imageList[k][r],modImageDirPath[k], r)

############################################################################################
# Image augmentation
def imageAugmentation(sourcePath,destPath,i):
    print(sourcePath)
    img = cv2.imread(sourcePath)
    # Translate Image
    M = np.float32([[1,0,10],[0,1,5]])
    translatedImage = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
    # save translated image
    saveImage(destPath, translatedImage,"translatedImage",i)
    # Rotate image
    R = cv2.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2),45,1)
    rotatedImage = cv2.warpAffine(img,R,(img.shape[1],img.shape[0]))
    # save rotated image
    saveImage(destPath, rotatedImage,"rotatedImage",i)
    # Crop image
    crop_Px = randint(0,25)
    croppedImage = img[crop_Px:img.shape[0]-crop_Px,crop_Px:img.shape[1]-crop_Px]
    # save cropped image
    saveImage(destPath, croppedImage,"croppedImage",i)
    # image resize
    resizedImage = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
    saveImage(destPath, resizedImage, "downsizeX2",i)
    
    # affineTransformation
    p1 = np.float32([[25,37.5],[100,25],[25,100]])
    p2 = np.float32([[25,50],[100,25],[50,125]])

    Mask1 = cv2.getAffineTransform(pts1,pts2)
    Mask2 = cv2.getAffineTransform(pts2,pts1)

    affineTransformed1 = cv2.warpAffine(img,M,(cols,rows))
    dst2 = cv2.warpAffine(img,M2,(cols,rows))
    
    # saving transformed image
    saveImage(destPath, dst1, "affine1",i)
    saveImage(destPath, dst2, "affine2", i)
    
    
############################################################################################
# Save Image
def saveImage(destPath, imageToSave,tranformationType, i):
    misc.imsave(destPath + tranformationType+"_"+str(i)+'.jpg', imageToSave)
    
############################################################################################
# Extract Data
def extractData():
    print("Extracting Data...")
    pathToImage =os.path.realpath("Dataset")
    imgPath = os.path.join(pathToImage,'*')
    fileList = glob.glob(imgPath)
    subFileList = []
    for i in range(len(fileList)):
        subDirectoryPath = os.path.join(fileList[i],'*');
        subFileList.append(glob.glob(subDirectoryPath))
    subNpArray = np.array(subFileList)
    imageList = []
    labelList = []
    mapList = []
    uniqueMapList = []
    key=0
    for i in range(len(subNpArray)):
        for j in range(len(subNpArray[i])):
            imageDirPath = os.path.join(subNpArray[i][j],'*.jpg')
            maplabels =  re.search('Dataset(.*)*.jpg', imageDirPath.replace("\\",""))
            maplabels = maplabels.group(0).split("Dataset",1)[1].replace("*.jpg","")
            imagePath = glob.glob(imageDirPath)
            for k in range(len(imagePath)):
                imageList.append(imagePath[0])
                labelList.append(key+1)
                mapList.append(maplabels)
            key+=1
            uniqueMapList.append(maplabels)
    imageNpArray = np.array(imageList)
    labelNpArray = np.array(labelList)
    mapNpArray = np.array(mapList)
    uniqueNpArray = np.array(uniqueMapList)
    np.savetxt('uniqueLabels.csv',uniqueNpArray,delimiter=',', fmt = '%s')
    np.savetxt('train_imagenames.csv',imageNpArray,delimiter=',', fmt = '%s')
    np.savetxt('train_labels.csv',labelNpArray,delimiter=',', fmt = '%s')
    np.savetxt('train_mapping.csv',mapNpArray,delimiter=',', fmt = '%s')
    print("Training Data and label created...")
############################################################################################
#createSyntheticImage()
extractData()
            
            

            
            
        

    
  

