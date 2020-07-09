import csv

with open('dataSet9.csv') as File:
    reader = csv.reader(File)
    x=0
    l=0
    array = []

    for row in reader:
        a = float(row[0])
        x=a+x
        array.append(a)

    media=(x/10000)
    print("Media: ",media)

    #Minimo valor en el array
    print("Minima: ",min(array))

    #Maximo valor en el array
    print("Maxima",max(array))
# Probabilidad de que la siguiente llamada sea en menos de 0.5 segundos

#Fuerza bruta
    for i in range(10000):
        if(array[i]<0.5):
            l=l+1
    print("Fuerza bruta :", (l / 10000))

#Exponencial
    e = 2.718281828459045
    exp = 1-pow(e,-(0.5/media))
    print("Distribucíon exponencial: ",exp)

print(max(array))
