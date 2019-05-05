
# coding: utf-8

# In[ ]:



#merge_info
labels=pd.read_csv("/content/stage_2_train_labels.csv")
classinfo=pd.read_csv("/content/stage_2_detailed_class_info.csv")
info1 =pd.concat([classinfo.drop(["patientId"],1), labels], 1)
info1.fillna(0, inplace=True)



