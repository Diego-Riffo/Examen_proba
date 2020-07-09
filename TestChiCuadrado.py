import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
import scipy.stats as ss
import math 


datosCsv = []
contador = 0
x=0
with open('dataSet9.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        contador = contador+1
        x=float(row[0])+x
        datosCsv.append(float(row[0]))

media=(x/10000)
datosCsvOrdenados = sorted(datosCsv)


lista1 = []
lista2=[]

#Numero de Intervalos = 14, #Por formula de sturges, pero entre mas intervalos, es mas representativo
AmplitudIntervalo=(max(datosCsvOrdenados)-min(datosCsvOrdenados))/16
#print(AmplitudIntervalo)

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
    
    #print(FrecIntervalo)
    FrecAbs+=FrecIntervalo

    lista1.append(datosCsvOrdenados[inicio])
    lista2.append(FrecIntervalo)
    if(IndiceCsv==10000-1):
        lista1.append(datosCsvOrdenados[IndiceCsv])
    #lista1.append(datosCsvOrdenados[IndiceCsv])


#Frecuencia de una funcion exponencial = Frecuencia esperada
#exp = 1-pow(e,-(0.5/media))
def FrecExponencial(media, start, final):
    return ((1-math.e **(-final/media))-(1-math.e **(-start/media)))*10000


T=0
print("Intervalo                                |          Frecuencia Obtenida                      |       Frecuencia esperada  |      X^2(Chi Cuadrado) Del intervalo")
print()
for z in range(len(lista2)):
    InicioIntervalo=lista1[z]
    FinIntervalo=lista1[z+1]
    FrecuenciObtenida=lista2[z]#Frecuencia sacada a partir del csv
    FrecuenciaEsperada=FrecExponencial(media, InicioIntervalo,FinIntervalo)#Frecuencia esperada segun distribucion Exponencial
    RelacionEntreLasFrecuencias=(math.pow(FrecuenciObtenida-FrecuenciaEsperada,2))/FrecuenciaEsperada
    T+=RelacionEntreLasFrecuencias
    #(Frecuencia Obtenida-Frecuencia esperada)^2)/Frecuencia Esperada
    print(InicioIntervalo, FinIntervalo,"                                "    ,   FrecuenciObtenida,"                                "  ,FrecuenciaEsperada,"                           ",RelacionEntreLasFrecuencias)
    #print(FrecExponencial(media, lista1[z],lista1[z+1]))   
print("Resultado de chi cuadrado es T : ",T)
#print("En la tabla de valores para Chi cuadrado, con 16-1=15 intervalos de confianza, tenemos una probabilidad de encontrar un valor mayor o igual que el chi cuadrado tabulado de : probabilidad menor a 0,05 con 15 intervalos es de  24.9958, mayor que el valor obtenido de chi 23.249, por lo que no se rechaza la hipótesis al nivel α = 0.05, lo que implica que en ese α, no da razon de no aceptar la hipotesis, pero si es menor que en el α=0,1, por lo que en el α=0,1 si se rechaza")