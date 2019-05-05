
# coding: utf-8

# In[ ]:

import pydicom
import os
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import seaborn as sns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#merge_info
labels=pd.read_csv("/content/stage_2_train_labels.csv")
classinfo=pd.read_csv("/content/stage_2_detailed_class_info.csv")
info1 =pd.concat([classinfo.drop(["patientId"],1), labels], 1)

info1.fillna(0, inplace=True)
images_list2=[]
for i in range(1,100):
  patID=info1.patientId.values[i]
  classification=info1.Target.values[i]
  path="/content/train_images/"+patID+".dcm"
  x=info1.x.values[i]
  y=info1.y.values[i]
  w=x+info1.width.values[i]
  h=y+info1.height.values[i]
  ds=pydicom.read_file("/content/train_images/"+patID+".dcm")
  images_list2.append([ds.pixel_array,path,classification,x,y,w,h])

#import display images
actual_images = []
for filename in glob.glob("/content/train_images/*.dcm"):
    ds=pydicom.read_file(filename)
    actual_images.append(ds)
