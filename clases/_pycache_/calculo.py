from collections import Counter
from turtle import pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
import math

datos = pd.read_csv("datosCriticapelicula.csv", sep =";")
class Calculo:
    def __init__(self, calcular):
        self.calcular = calcular
    
    def Media(self):
        n = self.calcular.count()
        sumaValores = 0
        media = 0
        for i in self.calcular:
            sumaValores = sumaValores + i
            
        media = sumaValores / n
        return media
