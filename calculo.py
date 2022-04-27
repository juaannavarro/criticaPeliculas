import csv
import numpy as np
import math
lista1 = []
lista2 = []
with open(file="datosCriticapelicula.csv", mode="r") as f:
    reader = csv.reader(f)
       
    for row in reader:
        print("Opciones: {0}, {1}" .format(row[0], row[1]))
        lista1.append(row[0])
        lista2.append(row[1])

print( "Columna 1: ", lista1)
print("Columna 2: ",lista2)



resultado= int(lista1[3])*int(lista2[3])
print("Resultado: ", resultado)








from collections import Counter
import matplotlib.pyplot as plt
class Estadistica:
    
        def __init__(self, caracteristica):
            self.caracteristica = caracteristica
            self.cantidad_valoraciones = np.array([42, 96, 132, 124, 88, 58])
            self.cantidad_valoraciones_ordenadas = np.sort(self.cantidad_valoraciones)
            self.cantidad_valoraciones_ordenadas_invertidas = np.sort(self.cantidad_valoraciones)[::-1]
            self.cantidad_valoraciones_ordenadas_invertidas_con_nan = np.sort(self.cantidad_valoraciones)[::-1]


        def percentiles(cantidad_valoraciones_ordenadas_invertidas_con_nan):
            cantidad_valoraciones = np.array([42, 96, 132, 124, 88, 58])
            p = np.percentile(cantidad_valoraciones, [68, 95, 97])
            return p
print(Estadistica.percentiles("cantidad_valoraciones_ordenadas_invertidas_con_nan"))