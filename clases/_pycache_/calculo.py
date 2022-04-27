from collections import Counter
from turtle import pd


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
