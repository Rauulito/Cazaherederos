import random

#Clase cuyas instancias se almacenaran en una base de datos
class Anuncio:
    def __init__(self, nombre, riesgo, vendedor):
        self.nombre = nombre
        self.riesgo = riesgo
        self.vendedor = vendedor

#Hacemos una funcion predefinida para determinar una clasificación de criptomonadas por su nivel de riesgo
#Como no tenemos ningun criterio definido vamos a hacerlo de forma aleatoria
def Nivel_Riesgo(nft):
    numero=random.randint(1,3)
    if numero==1:
        riesgo="Bajo"
    elif numero==2:
        riesgo="Medio"
    else:
        riesgo="Alto"
    return riesgo

print(Nivel_Riesgo("luis"))#Prueba para que funcione Nivel_Riesgo