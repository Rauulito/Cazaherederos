import sqlite3

#Este programa solo sirve para generar la Base de Datos vacía donde después, y mediante otros programas
# se guardaran los anuncios que se vayan publicando

##############################################################################################################
# IMPORTANTE: SOLO HAY QUE EJECUTARLO UNA VEZ, Y ANTES DE EMPEZAR A EJECUTAR OTROS PROGRAMAS QUE LA UTILICEN #
##############################################################################################################

# Objeto que representa la conexión a la base.
conexion = sqlite3.connect('anuncios.db')

# Uso de la palabra clave 'with' que cerrará automáticamente la conexión al final del bloque.
with conexion:

    # Recuperación del cursor de la conexión.
    cursor = conexion.cursor()

    # Ejecución de un script SQL para crear una tabla.
    # Esta TABLA se llama Anuncios y contiene las siguientes columnas:
    #    un Identificador entero que debe ser único entre todos, sera clave autoincrementada
    #    el Nombre del NFT como campo de texto
    #    el Nivel de Riesgo del NFT como campo de texto
    #    el Vendedor que publica el anuncio como campo de texto

    orden="CREATE TABLE Anuncios(Id INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, Riesgo TEXT, Vendedor TEXT)"
    cursor.execute(orden)