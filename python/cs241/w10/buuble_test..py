alist = [54,26,93,17,77,31,44,55,20]
'''for f in range((len(alist))-1,0,-1):
    print(alist[f])
print("comparar elementos adyacentes")
for f in range((len(alist))-1,0,-1):    
    if alist[f] > alist[f-1]:
            print("horay",alist[f])
print("iterando 2 veces sin variar orden")
for f in range((len(alist))-1,0,-1):    
    for i in range(f):
        print(alist[i]," and ",alist[i+1])
print("Verificar cual es mayor iterando 2 veces")
for f in range((len(alist))-1,0,-1):    
    for i in range(f):
        if alist[i] > alist[i]+1:
            print(alist[i])        '''   
print("variando orden de la lista")
print(alist)
def bubleSort(alist):
    for f in range(len(alist)-1,0,-1):    
        for i in range(f):
            if alist[i] > alist[i+1]:
                temporal = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temporal
                print(alist)     
print(alist)
bubleSort(alist)
print(alist)