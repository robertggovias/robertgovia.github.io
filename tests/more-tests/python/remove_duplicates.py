def remove_duplicates(x):
  z=[]
  t=0
  for i in x:
    if i not in z: 
      z.append(i)
  return z
print remove_duplicates([1,1,1,4,4,4,2,2,3,3,3,4])
