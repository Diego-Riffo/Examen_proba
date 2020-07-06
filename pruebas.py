
lista1=[1,2,3,4,5,6]
lista2Frec=[0,1,2,0,0,0]

contador=0
for i in range(len(lista2Frec)):   
    if(lista2Frec[i-contador]==0):
        lista1.remove(lista1[i-contador])
        lista2Frec.remove(lista2Frec[i-contador])
        contador+=1

print(lista1)
print(lista2Frec)