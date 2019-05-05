
# coding: utf-8

# In[ ]:



pneumonia_locations={}
for i in range(1,len(labels)):
  target=labels.Target[i]
  if target==1:
    name=labels.patientId[i]
    location=labels.x[i],labels.y[i],labels.width[i],labels.height[i]
    if name in pneum_locs:
      pneumonia_locations[name].append(location)
    else:
      pneumonia_locations[name] = [location]

