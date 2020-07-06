import csv

with open('dataSet9.csv') as File:
    reader = csv.reader(File)
    x=0
    array = []

    for row in reader:
        a = float(row[0])
        x=a+x
        array.append(a)

    media=(x/10000)
    print(media)
    print(min(array))
    print(max(array))
    print(array[0])
