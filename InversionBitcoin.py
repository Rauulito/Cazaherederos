#hacemos una funcion para ver cuando el valor de bitcoin cae por debajo de 30000
def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    if(euros_value < 30000):
        print("El valor de euros es menor que 30000")
    return euros_value

#Probamos la funcion metiendo los datos por teclado
bitcoin_amount = int(input("Introduce la cantidad de bitcoin: ")) #leemos la cantidad de bitcoin
bitcoin_value_euros = float(input("Introduce el valor de bitcoin en euros: ")) #leemos el valor de bitcoin en euros
euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros) #llamamos a la funcion100
print("El valor de euros es: ", euros_value)