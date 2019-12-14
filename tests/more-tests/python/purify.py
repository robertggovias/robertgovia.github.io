def purify(x):
  r=[]
  d=0
  for i in x:
    if i%2==0:
      r.append(i)
  return r
print purify([2,4,6,5,7,8])