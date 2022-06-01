import sqlite3

# Objeto que representa la conexión a la base.
conexion = sqlite3.connect('anuncios.db')

# Uso de la palabra clave 'with' que cerrará automáticamente la conexión al final del bloque.
with conexion:

    # Recuperación del cursor de la conexión.
    cursor = conexion.cursor()

    # Ejecución de un script SQL para crear una tabla.


    orden="CREATE TABLE Anuncio(Id INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, Riesgo TEXT, Vendedor TEXT)"
    cursor.execute(orden)