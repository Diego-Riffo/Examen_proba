import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import scipy.stats as ss


datosCsv = []
contador = 0
with open('dataSet9.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        contador = contador+1
        # print(row)
        datosCsv.append(float(row[0]))


datosCsvOrdenados = sorted(datosCsv)
print(len(datosCsvOrdenados))
print(contador)

lista1 = []
lista2=[]

#Numero de Intervalos = 14, #Por formula de sturges, pero entre mas intervalos, es mas representativo
AmplitudIntervalo=(max(datosCsvOrdenados)-min(datosCsvOrdenados))/100
print(AmplitudIntervalo)

IndiceCsv=0
IndiceCsv2=0
FrecAbs=0
for i in range(100):
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
    lista2.append(((FrecIntervalo/10000))/AmplitudIntervalo)
    lista1.append(datosCsvOrdenados[IndiceCsv])
    lista2.append(((FrecIntervalo/10000))/AmplitudIntervalo)



print("Comenzaremos a graficar")
print(len(lista1))
print(len(lista2))
print(FrecAbs)
plt.plot(lista1, lista2)
plt.xlabel('Tiempos')
plt.ylabel('Densidad')
plt.title('Examen Proba')

plt.show()
