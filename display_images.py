
# coding: utf-8

# In[ ]:


actual_images = []
for filename in glob.glob("/content/train_images/*.dcm"):
    ds=pydicom.read_file(filename)
    actual_images.append(ds)
	
#display
def plot(k):
    ds=actual_images[k]
    boxes=info1.loc[info1['patientId'] == str(ds[0x010, 0x010].value)]
    len=boxes.patientId.count()
    print(boxes)
    plt.figure()
    for i in range(0,len):
        fig=plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
        ax = plt.gca()
        rect = plt.Rectangle((boxes["x"].iloc[i], boxes["y"].iloc[i]), boxes["width"].iloc[i], boxes["height"].iloc[i], edgecolor='b',linewidth=2, alpha=0.2,fill=None)
        ax.add_patch(rect)
    plt.show()

