import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import expon
import math

def exp(datoX, media):
    exp = (1/media)* math.e **(-datoX/media)
    return exp



datosCsv=[]
contador=0
x=0
with open('dataSet9.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        contador=contador+1
        #print(row)
        x=float(row[0])+x
        datosCsv.append(float(row[0]))

   
print(contador)#cantidad de datos en el csv
media=(x/10000)
print("Media: ",media)

cantElementos=max(datosCsv)-min(datosCsv)
cantElementos2=int(cantElementos*1000000)
#print(cantElementos)
print(cantElementos2)

expX=[]
expY=[]
#Setear las listas con los valores correspondientes
for i in range(cantElementos2):
    expX.append(0.000002+0.000001*i)
    expY.append(exp(0.000002+0.000001*i, media))


print("Hola wapo, comenzaremos a graficar")
print(len(expX))
print(len(expY))
plt.plot(expX,expY)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.title('Examen Proba')
plt.show()
