
# coding: utf-8

# In[ ]:


folder="/content/train_images/"
pneum_locs=[]
filenames=[]
for filename in glob.glob("/content/train_images/*.dcm"):
  ds=pydicom.read_file(filename)
  boxes = info1[(info1['patientId'] == str(ds[0x010, 0x010].value)) & (info1['class'] == 'Lung Opacity')]
  pneumonia_loc = boxes.iloc[:,2:6].values
  filenames.append(str(ds[0x010, 0x010].value))
  if len(pneumonia_loc)>0:
    pneum_locs.append([str(ds[0x010, 0x010].value),pneumonia_loc])

