import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange

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
lista1 = []
lista2Frec = []

# Llenar los ejes

#Se ordena los datos de forma creciente, para que cuando se cuenten las veces 
#que se repite un dato en el csv, no se tenga que recorrer todo el csv
# y solo tener que revisar el siguiente dato a leer, ya que estan agrupados por orden
datosCsvOrdenados = sorted(datosCsv)
print(len(datosCsvOrdenados))

#El cont es para ir restando a la lista 1 y 2 el indice i, ya que eston tendras menos elementos
#que el csv, ya que solo tendra solo 1 vez el dato
cont = 1
#El contador parte de 1, porque el i=0 se no "muere" en la condicion
# de que la lista 1 esta vacia(primer if), para que la parte de operaciones del codigo
#que es en else mas exterior, el primer if, no se nos salga del rango de las listas
for i in range(contador):
    if len(lista1) == 0:
        print("Entra a 0")
        lista1.append(datosCsvOrdenados[i])
        lista2Frec.append(1)
        print("len 1 :"+str(len(lista1)))
        print("len 2 :"+str(len(lista2Frec)))
    else:
        if lista1[i-cont] == datosCsvOrdenados[i]:
            print("Entra a 1")
            lista2Frec[i-cont] += 1
            cont += 1
        else:
            print("Entra a 2")
            lista1.append(datosCsvOrdenados[i])
            lista2Frec.append(1)


print("Hola wapo, comenzaremos a graficar")
print(len(lista1))
print(len(lista2Frec))
plt.scatter(lista1, lista2Frec)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.title('Examen Proba')
plt.yticks(range(6))
plt.xticks(arange(0.0, 3, 0.5))
plt.show()
