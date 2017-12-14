
# coding: utf-8

# In[27]:


import numpy as np
import os
import glob
import re

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
                imageList.append(imagePath[k])
                labelList.append(key+1)
                mapList.append(maplabels)
            key+=1
            uniqueMapList.append(maplabels)
    imageNpArray = np.array(imageList)
    labelNpArray = np.array(labelList)
    mapNpArray = np.array(mapList)
            
    print(uniqueMapList)
    uniqueNpArray = np.array(uniqueMapList)
    #with open('uniqueLabels.csv','wb') as f:
     #   np.savetxt(f,uniqueNpArray, fmt = '%s')
    np.savetxt('uniqueLabels.csv',uniqueNpArray,delimiter=',', fmt = '%s')
    np.save("input",imageNpArray)
    np.save("output",labelNpArray)
    np.save("map",mapNpArray)

#    def augmentData(imageNpArray):
    
    print("Training Data and label created...")

extractData()
            
            

            
            
        

    
  


# In[ ]:




