import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import expon
import math

def exp(datoX, media):
    return (1/media)* math.e **-(datoX/media)



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


expX=[]
expY=[]
#Setear las listas con los valores correspondientes
datosCsvOrd=sorted(datosCsv)
for i in range(contador):
    expX.append(datosCsvOrd[i])
    expY.append(exp(datosCsvOrd[i], media))


print("Hola wapo, comenzaremos a graficar")
print(len(expX))
print(len(expY))
plt.plot(expX,expY)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.title('Examen Proba')
plt.show()
