import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
import math
from numpy import arange


############ Leyendo y almacenando datos del CSV########################
datosCsv = []
contador = 0
x=0
with open('dataSet9.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        contador=contador+1
        x=float(row[0])+x
        datosCsv.append(float(row[0]))




#################      Histograma a partir de los datos del CSV          ###############
datosCsvOrdenados = sorted(datosCsv)


lista1 = []
lista2=[]

#Numero de Intervalos = 14, #Por formula de sturges, pero entre mas intervalos, es mas representativo
#pero para que todos los intervalos tengan el mismo rango, se eligira 16, ya que 10.000/16=625, un entero
AmplitudIntervalo=(max(datosCsvOrdenados)-min(datosCsvOrdenados))/16

IndiceCsv=0
IndiceCsv2=0

for i in range(16):
    inicio=IndiceCsv
    FrecIntervalo=0
    while(datosCsvOrdenados[IndiceCsv]<(datosCsvOrdenados[inicio]+AmplitudIntervalo)):
        IndiceCsv+=1
        FrecIntervalo+=1
        if(IndiceCsv==10000):
            IndiceCsv-=1
            break


    lista1.append(datosCsvOrdenados[inicio])
    lista2.append(((FrecIntervalo/10000))/AmplitudIntervalo)
    lista1.append(datosCsvOrdenados[IndiceCsv])
    lista2.append(((FrecIntervalo/10000))/AmplitudIntervalo)

plt.plot(lista1, lista2)


######################### Exponencial #############################
def exp(datoX, media):
    exp = (1/media)* math.e **(-datoX/media)
    return exp


media=(x/10000)
expX=[]
expY=[]
#Llenar las listas con los valores de al distribucion binomial
datosCsvOrd=sorted(datosCsv)
for i in range(contador):
    expX.append(datosCsvOrd[i])
    expY.append(exp(datosCsvOrd[i], media))


plt.plot(expX,expY)
plt.xlabel('Datos')
plt.ylabel('Densidad')
plt.title('Examen Proba')
plt.show()

