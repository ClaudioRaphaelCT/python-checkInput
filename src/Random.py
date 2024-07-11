import random

class Random:
    @classmethod
    def gerar_numero_aleatorio(cls):
        numero_aleatorio = str(random.randint(1000,9999))
        array_aleatrio = list(numero_aleatorio)
        print(array_aleatrio)
        return array_aleatrio
    
   
    