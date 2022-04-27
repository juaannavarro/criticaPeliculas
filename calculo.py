import csv

with open(file="datosCriticapelicula.csv", mode="r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("Opciones: {0}, {1}".format(row[0], row[1]))
        print(row.index[3])








from collections import Counter
from math import *
import matplotlib.pyplot as plt
class Estadistica:
    
        def __init__(self, caracteristica):
            self.caracteristica = caracteristica
    
        def calculoMediaAritmetica(self):
            n = self.caracteristica.count()
            sumaValoresObservaciones = 0
            mediaAritmetica = 0
            for valorObservacion in self.caracteristica:
                sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion
    
            mediaAritmetica = sumaValoresObservaciones / n
            return mediaAritmetica
    
        def calculoMediana(self):
            mediana = 0
            caracteristica = self.caracteristica.sort_values()
            caracteristica = caracteristica.reset_index(drop=True)
            n = self.caracteristica.count()
            par = False;
            if (n % 2 == 0):
                print("La cantidad de observaciones es par.")
                par = True
    
            if par:
                rango = (n / 2);
                print("RANGO = " + str(rango))
                rangoPython = rango - 1
                valor1 = caracteristica[rangoPython]
                valor2 = caracteristica[rangoPython + 1]
                mediana = valor1 + ((valor2 - valor1) / 2)
            else:
                rango = ((n + 1) / 2)
                rangoPython = rango - 1
                mediana = caracteristica[rangoPython]
    
            return [mediana, rango]
    
        def calculoModa(self):
            moda = Counter(self.caracteristica)
            return moda
    
        def calculoVarianzaDesviacionTipica(self):
            n = self.caracteristica.count()
            mediaAritmetica = self.caracteristica.mean()
            varianza = 0
            c3 = 0
            for valorObservacion in self.caracteristica:
                x = valorObservacion
                moy = mediaAritmetica
                c1 = valorObservacion - mediaAritmetica
                c2 = c1 ** 2
                c3 = c3 + c2
            varianza = c3 / n
            desviacionTipica = sqrt(varianza)
            return [varianza, desviacionTipica]
        def percentiles(self, percentiles):
            caracteristica = self.caracteristica.sort_values()
            caracteristica = caracteristica.reset_index(drop=True)
            n = self.caracteristica.count()
            par = False;
            if (n % 2 == 0):
                print("La cantidad de observaciones es par.")
                par = True
    
            if par:
                rango = (n / 2);
                print("RANGO = " + str(rango))
                rangoPython = rango - 1
                valor1 = caracteristica[rangoPython]
                valor2 = caracteristica[rangoPython + 1]
                mediana = valor1 + ((valor2 - valor1) / 2)
            else:
                rango = ((n + 1) / 2)
                rangoPython = rango - 1
                mediana = caracteristica[rangoPython]
    
            return [mediana, rango]

        def analisisCaracteristica(self):
    
            print("-----------------------------------------")
            print("      MEDIDA DE TENDENCIA CENTRAL        ")
            print("-----------------------------------------\n")

            print("-- CANTIDAD DE OBSERVACIONES --")
        # -Cantidad de observaciones
            n = self.caracteristica.count()
            print("Cantidad de observaciones = " + str(n))

            print ("\n-- MIN --")
            valoresOrdenados = self.caracteristica.sort_values()
            valoresOrdenados = valoresOrdenados.reset_index(drop=True)
            print("Valor mínimo: "+str(valoresOrdenados[0]))

            print ("\n-- MAX --")
            valoresOrdenados = self.caracteristica.sort_values()
            valoresOrdenados = valoresOrdenados.reset_index(drop=True)
            print("Valor máximo: " + str(valoresOrdenados[len(valoresOrdenados)-1]))

        # -Media artimética:
            print("\n-- MEDIA --")
            media = self.calculoMediaAritmetica()
            print("Media aritmética calculada = " + str(media))
            print("> Observaciones: Si todas las observaciones tuvieran el mismo valor (reparto equitativo), este sería " + str(media))

        # -Media aritmética:
            print("\n-- MEDIANA --")
            mediana = self.calculoMediana()
            print("Mediana calculada = " + str(mediana[0]))
            print("> Observaciones: El valor que se encuentra en el punto medio de las observaciones es:" + str(mediana[0]))
            print("El reparto es: " + str(mediana[1]) + " valores en cada lado de la mediana")

        # -Moda
            print("\n-- MODA --")
            moda = self.calculoModa()
            print(moda)
            print("> Observacions: La moda permite determinar los valores observados con más frecuencia")


            print("\n\n-----------------------------------------")
            print("      MEDIDA DE DISPERSION        ")
            print("-----------------------------------------\n")
            print("-- RANGO --")
            print ("Rango de la serie = "+str(valoresOrdenados[len(valoresOrdenados)-1]-valoresOrdenados[0]))
            varianzaDesviacionTipica = self.calculoVarianzaDesviacionTipica()

            print("\n-- VARIANZA --")
            print("Varianza calculada = " + str(varianzaDesviacionTipica[0]))

            print("\n-- DESVIACION TIPICA --")
            print("Desviación típica calculada = " + str(varianzaDesviacionTipica[1]))
            desviacionTipica = varianzaDesviacionTipica[1]
            print("68 % de los valores de las observaciones se sitúan entre " + str(media - desviacionTipica) + " y " + str(
            media + desviacionTipica))
            print("95 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 2)) + " y " + str(
            media + (desviacionTipica * 2)))
            print("99 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 3)) + " y " + str(
            media + (desviacionTipica * 3)))

            print("\n\n-----------------------------------------")
            print("      CUARTILES        ")
            print("-----------------------------------------\n")
            cuartiles = self.calculoDelosCuartiles(mediana[0],mediana[1])
            print("25 % de las observaciones tienen un valor inferior a " + str(cuartiles[0]))
            print("50 % de las observaciones tienen un valor inferior a " + str(cuartiles[1]))
            print("75 % de las observaciones tienen un valor inferior a " + str(cuartiles[2]))


            print("\n\n-----------------------------------------")
            print("      DETECCION VALORES ABERRANTES        ")
            print("-----------------------------------------\n")
            print("> Criterios de Tukey")
            valoresAberrantes = self.criterioDeTukey(cuartiles[0], cuartiles[2])
            print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
            print("Valores:" + str(valoresAberrantes))


            print("\n\n-----------------------------------------")
            print("      VISUALIZACION        ")
            print("-----------------------------------------\n")
            print("Generación de las gráficas...")
            self.visualizacion(media,mediana[0],cuartiles[0],cuartiles[1],cuartiles[2])

print("\n\n-----------------------------------------")
print("      CARACTERISTICAS        ")
print("-----------------------------------------\n")

print(Estadistica.calculoMediaAritmetica(self))
print(Estadistica.calculoMediana(self))
print(Estadistica.calculoModa(self))
print(Estadistica.calculoVarianzaDesviacionTipica(self))
print(Estadistica.percentiles(self))


