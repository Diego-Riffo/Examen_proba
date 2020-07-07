import csv
import matplotlib.pyplot as plt
import numpy as np
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


#################  Graficar la distribucion exp con el ajuste de la media############################

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



#################  Graficar los Datos ############################

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
        lista1.append(datosCsvOrdenados[i])
        lista2Frec.append(1)
    else:
        if lista1[i-cont] == datosCsvOrdenados[i]:
            lista2Frec[i-cont] += 1
            cont += 1
        else:
            lista1.append(datosCsvOrdenados[i])
            lista2Frec.append(1)


print("Hola wapo, comenzaremos a graficar")
print(len(lista1))
print(len(lista2Frec))
plt.scatter(lista1, lista2Frec)
plt.plot(expX,expY)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.title('Examen Proba')
plt.yticks(range(6))

#plt.xticks(arange(0.0, 3, 0.5))
#ss.expon.sf(0.3,loc=0,scale=1) 
plt.show()