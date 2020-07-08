import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
import math
from numpy import arange


def exp(datoX, media):
    exp = (1/media)* math.e **(-datoX/media)
    return exp


datosCsv = []
contador = 0
x=0
with open('dataSet9.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        contador=contador+1
        #print(row)
        x=float(row[0])+x
        datosCsv.append(float(row[0]))


datosCsvOrdenados = sorted(datosCsv)
print(len(datosCsvOrdenados))
print(contador)
lista1 = []
lista2=[]

##Numero de intervalos = 25

AmplitudIntervalo=(max(datosCsvOrdenados)-min(datosCsvOrdenados))/25
print(AmplitudIntervalo)

IndiceCsv=0
IndiceCsv2=0
FrecAbs=0
for i in range(25):
    inicio=IndiceCsv
    FrecIntervalo=0
    while(datosCsvOrdenados[IndiceCsv]<(datosCsvOrdenados[inicio]+AmplitudIntervalo)):
        IndiceCsv+=1
        FrecIntervalo+=1
        if(IndiceCsv==10000):
            IndiceCsv-=1
            break
    
    print(FrecIntervalo)
    FrecAbs+=FrecIntervalo

    lista1.append(datosCsvOrdenados[inicio])
    lista2.append(FrecIntervalo/1000)
    lista1.append(datosCsvOrdenados[IndiceCsv])
    lista2.append(FrecIntervalo/1000)

plt.plot(lista1, lista2)


############### Exponencial ###################
   
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

