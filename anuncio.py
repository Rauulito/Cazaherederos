import random
import sqlite3
from threading import Thread

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


#Hacemos una funcion predefinida para determinar si a un cliente le interesa un anuncio o no
#Como no tenemos ningun criterio definido vamos a hacerlo de forma aleatoria(devolvera True si le interesa y false si no le interesa)
def Interesa(nft, cliente):
    numero=random.randint(1,2)
    if numero==1:
        interesa=True
    else:
        interesa=False
    return interesa



# Metodo para publicar un anuncio
def publicar(anuncio):
    # Objeto que representa la conexión a la base.
    conexion = sqlite3.connect('anuncios.db')
    # Uso de la palabra clave 'with' que cerrará automáticamente
    # la conexión al final del bloque.
    with conexion:
        # Recuperación del cursor de la conexión
        cursor = conexion.cursor()
        # ... ejecutamos un script SQL que insertará uno nuevo
        # registro en la tabla
        cursor.execute("INSERT INTO Anuncios (Nombre, Riesgo, Vendedor) VALUES(?,?,?)",
                        (anuncio.nombre, Nivel_Riesgo(anuncio.nombre),
                        anuncio.vendedor))
        # Las acciones de escritura no se realizan de forma inmediata
        # en la base. El método commit() valida las modificaciones
        conexion.commit ()

# Mostramos los datos del anuncio insertado para ver cuando va ejecutandose cada hilo de publicar
    print("Publicado anuncio del NFT:", anuncio.nombre, "- por el vendedor:", anuncio.vendedor)

def comprar(riesgo,comprador):
    # Objeto que representa la conexión a la base.
    conexion = sqlite3.connect('anuncios.db')
    # Uso de la palabra clave 'with' que cerrará automáticamente
    # la conexión al final del bloque.
    with conexion:
        # Recuperación del cursor de la conexión.
        cursor = conexion.cursor()
        # ... ejecutamos un script SQL que consultaá los
        # registros en la tabla con el riesgo indicado
        cursor.execute("SELECT * FROM Anuncios WHERE Riesgo =?",
                        (riesgo,))
        # La solicitud se ejecuta y obtenemos la lista de los que cumplen el riesgo indicado
        lineas = cursor.fetchall()
        Encuentra = "NO"
        # Se recorre esta lista de registros...
        for linea in lineas:
            # ... y se muestran en la salida estándar.
            print(linea[0], linea[1])
            Interes = (Interesa(linea[1],comprador))
            print (Interes)
            if (Interes):
                # Se le notifica al vendedor, aqui lo haremos mostrando un mensaje
                print("***AVISO AL VENDEDOR:", linea[3])
                print("***Le interesa el anuncio del NFT:", linea[1], "- al comprador:", comprador)
                # ... ejecutamos un script SQL que borrará el anuncio que le interesa al comprador
                cursor.execute("DELETE FROM Anuncios WHERE Id =?",
                                (linea[0],))
                # Las acciones de escritura no se realizan de forma inmediata
                # en la base. El método commit() valida las modificaciones
                conexion.commit ()
                Encuentra = "SI"
                break # Se sale del bucle porque ya ha encontrado uno que le interesa
        if (Encuentra=="SI"):
            print("Se elimina el anuncio del NFT:", linea, "- lo ha comprado:", comprador) #Mostramos el anuncio eliminado
        else:
            print("No se ha podido comprar NFT de riesgo:", riesgo, "solicitado por el comprado:", comprador) #Mostramos el nft que no se ha podido comprar

if __name__ == '__main__':

    #Probamos la funcion publicar con dos hilos simultaneos
    A1 = Anuncio("NFT_001", "", "Vendedor01")
    A2 = Anuncio("NFT_002", "", "Vendedor01")

    t1 = Thread(target=publicar,args=(A1,))
    t2 = Thread(target=publicar,args=(A2,))

    t1.start()
    t2.start()

