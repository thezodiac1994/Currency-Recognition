
# coding: utf-8

# In[89]:


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
for i in range(len(subNpArray)):
    for j in range(len(subNpArray[i])):
        imageDirPath = os.path.join(subNpArray[i][j],'*.jpg')
        labels =  re.search('Dataset(.*)*.jpg', imageDirPath.replace("\\",""))
        labels = labels.group(0).split("Dataset",1)[1].replace("*.jpg","")
        imagePath = glob.glob(imageDirPath)
        for k in range(len(imagePath)):
            imageList.append(imagePath[k])
            labelList.append(labels)
imageNpArray = np.array(imageList)
labelNpArray = np.array(labelList)
np.savetxt('train_imagenames.csv', imageNpArray, delimiter=",", fmt="%s")
np.savetxt('train_labels.csv', labelNpArray, delimiter=",", fmt="%s")

#np.savetxt("output.csv",labelNpArray, delimiter = ",")
print("Training Data and label created...")



            
            
        

    
  


# In[ ]:




