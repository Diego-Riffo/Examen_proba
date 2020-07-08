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


#Estas listas son los ejes de la grafica, lista 1 =ejex ; lista2=eje y
#Donde en la lista 1 va el dato y en la lista 2, la frecuencia del dato i de la lista1
datosCsvOrdenados = sorted(datosCsv)
print(len(datosCsvOrdenados))
print(contador)

lista1 = []
lista2=[]
#Formula de Sturges, numero de intervalos =16

AmplitudIntervalo=(max(datosCsvOrdenados)-min(datosCsvOrdenados))/16
print(AmplitudIntervalo)

IndiceCsv=0
IndiceCsv2=0
FrecAbs=0
for i in range(16):
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
    lista2.append(FrecIntervalo/10000)
    lista1.append(datosCsvOrdenados[IndiceCsv])
    lista2.append(FrecIntervalo/10000)



#print(lista2)




print("Hola wapo, comenzaremos a graficar")
print(len(lista1))
print(len(lista2))
print(FrecAbs)
plt.plot(lista1, lista2)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.title('Examen Proba')
#plt.yticks(range(6))

#plt.xticks(arange(0.0, 3, 0.5))
plt.show()
