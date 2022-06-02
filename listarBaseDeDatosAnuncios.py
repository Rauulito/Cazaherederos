import sqlite3

# Metodo para listar la base de datos
def vertodo():
    # Objeto que representa la conexión a la base.
    conexion = sqlite3.connect('anuncios.db')
    # Uso de la palabra clave 'with' que cerrará automáticamente
    # la conexión al final del bloque.
    with conexion:
        # Recuperación del cursor de la conexión.
        cursor = conexion.cursor()
        # Ejecutamos una consulta para recuperar todos los
        # registros (simbolizados por el carácter asterisco)
        # de la tabla.
        cursor.execute ("SELECT * FROM Anuncios")
        # La solicitud se ejecuta y de hecho obtenemos
        # la lista completa en una variable.
        lineas = cursor.fetchall()

    # Se recorre esta lista de registros...
    for linea in lineas:
        # ... y se muestran en la salida estándar.
        print(linea)

if __name__== '__main__':

    vertodo()
