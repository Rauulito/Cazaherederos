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
print(Nivel_Riesgo("nft"))#Prueba para  ver que funcione Nivel_Riesgo

#Hacemos una funcion predefinida para determinar si a un cliente le interesa un anuncio o no
#Como no tenemos ningun criterio definido vamos a hacerlo de forma aleatoria(devolvera True si le interesa y false si no le interesa)
def Interesa(nft, cliente):
    numero=random.randint(1,2)
    if numero==1:
        interesa=True
    else:
        interesa=False
    return interesa
print(Interesa("nft", "cliente"))#Prueba para ver que funcione Interesa
