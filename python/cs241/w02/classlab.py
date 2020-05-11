a = open("list.csv",'r')
b = a.readlines()
z=[]
#b = a.readlines()
#f = b.split(",")
print(b)

for c in b:
    f= c.split(",")   
    z.append(f[6])
zp = z[1:len(z)]
pp=0
for y in zp:   
    j=float(y)
    pp+=j

sumin=pp/len(zp)

minimo=min(zp)
maximo=max(zp)

minimo_index=zp.index(minimo)
maximo_index=zp.index(maximo)
miin=b[minimo_index+1].split(",")
maax=b[maximo_index+1].split(",")

pmiin = "{} ({}, {}) - ${}".format(miin[2],miin[0],miin[3],miin[6])
pmaax = "{} ({}, {}) - ${}".format(maax[2],maax[0],maax[3],maax[6])

print(f)
print("ahora z")
print(z)

print("ahora min")
print (min(zp))
print("min index")
print(zp.index(min(zp)))

print("ahora max")
print (max(zp))
print("max index")
print(zp.index(max(zp)))

print("datos min")
print(pmiin)


print("datos max")
print(pmaax)

print("sumatoria")
print(sumin)