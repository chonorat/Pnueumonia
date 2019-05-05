
# coding: utf-8

# In[1]:



#this code just imports data from kaggle to google colab
for i in range (1,3):
  get_ipython().system('pip install -U pydicom')
  key={"username":"chonorat","key":"372dd2c0fad0556f067a3eb0452e8f77"}
  import json
  out_file = open("kaggle.json",'w+') 
  json.dump(key,out_file) 
  get_ipython().system('pip install -U -q kaggle')
  get_ipython().system('mkdir -p ~/.kaggle')
  get_ipython().system('cp kaggle.json ~/.kaggle/')
  get_ipython().system('kaggle datasets list')
get_ipython().system('kaggle competitions download -c rsna-pneumonia-detection-challenge')
get_ipython().system('unzip stage_2_train_images.zip -d train_images')
get_ipython().system('unzip stage_2_test_images.zip -d test_images')
get_ipython().system('unzip stage_2_detailed_class_info.csv.zip ')
get_ipython().system('unzip stage_2_train_labels.csv.zip')

