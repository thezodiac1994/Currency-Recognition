
# coding: utf-8

# In[13]:


import numpy as np
import os
import glob
import re

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
imageNpArray = np.array(imageList)
labelNpArray = np.array(labelList)
mapNpArray = np.array(mapList)
np.save("input",imageNpArray)
np.save("output",labelNpArray)
np.save("map",mapNpArray)
print("Training Data and label created...")
            
            

            
            
        

    
  


# In[ ]:




