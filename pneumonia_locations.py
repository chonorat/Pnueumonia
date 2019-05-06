
# coding: utf-8

# In[ ]:

# empty dictionary
pneumonia_loc = {}
for i in range(1,len(info1)):
  filename = info1.patientId[i]
  location = info1.x[i],info1.y[i],info1.width[i],info1.height[i]
  pneumonia = info1.Target[i]
  if pneumonia == 1:
    location = [int(float(i)) for i in location]
    if filename in pneumonia_loc:
      pneumonia_loc[filename].append(location)
    else:
      pneumonia_loc[filename] = [location]
