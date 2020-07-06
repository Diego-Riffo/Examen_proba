import csv
import matplotlib.pyplot as plt
import numpy as np
 
datosCsv=[]
contador=0
with open('dataSet9.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        contador=contador+1
        #print(row)
        datosCsv.append(float(row[0]))
    
print(contador)#cantidad de datos en el csv
'''
#print(datosCsv)
print(sorted(datosCsv))
print(max(datosCsv))
print(min(datosCsv))
'''
cantElementos=max(datosCsv)-min(datosCsv)
cantElementos2=int(cantElementos*1000000)
#print(cantElementos)
print(cantElementos2)

lista1=[]
lista2Frec=[]
#Setear las listas con los valores correspondientes
for i in range(cantElementos2):
    lista1.append(0.000002+0.000001*i)
    lista2Frec.append(0)

#print(lista1)
#print(lista2Frec)

print("Paso al for 2")
#Modificar las listas con los valores del csv
for i in range(cantElementos2):        
    while(lista1[i] in datosCsv):
            lista2Frec[i]+=1
            datosCsv.remove(lista1[i])
'''
print("Paso al for 3")
#Limpiamos los 0
contador=0
for i in range(len(lista2Frec)):   
    if(lista2Frec[i-contador]==0):
        lista1.remove(lista1[i-contador])
        lista2Frec.remove(lista2Frec[i-contador])
        contador+=1
'''

print("Hola wapo, comenzaremos a graficar")
print(len(lista1))
print(len(lista2Frec))
plt.plot(lista1,lista2Frec,'ro')
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.title('Examen Proba')
plt.show()
