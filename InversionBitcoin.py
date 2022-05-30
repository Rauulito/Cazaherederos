def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros): #hacemos una funcion para ver cuando el valor de bitcoin cae por debajo de 30000
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value
    if(euros_value < 30000):
        print("El valor de euros es menor que 30000")