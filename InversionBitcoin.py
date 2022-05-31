from tkinter import *
from tkinter import ttk
import tkinter as tk

#hacemos una funcion para ver cuando el valor de bitcoin cae por debajo de 30000
def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    if(euros_value < 30000):
        print("El valor de euros es menor que 30000")
    return euros_value

#Probamos la funcion metiendo los datos por teclado
bitcoin_amount = int(input("Introduce la cantidad de bitcoin: ")) #leemos la cantidad de bitcoin
bitcoin_value_euros = float(input("Introduce el valor de bitcoin en euros: ")) #leemos el valor de bitcoin en euros
euros_value = bitcoinToEuros(bitcoin_amount, bitcoin_value_euros) #llamamos a la funcion(calcula valor de los bitcoins en euros)
print("El valor de euros es: ", euros_value)

#Probamos la funcion mediante interfaz grafica(tkinter)
#Metodo para calcular la multiplicacion
def multiplicacion():
    multiplicacion=int(entrada1.get())*int(entrada2.get())
    return var.set(multiplicacion)

#Metodo para cerrar
def cerrar():
    ventana.destroy()


ventana = tk.Tk() #creamos la ventana
ventana.title("Inversion en Bitcoin") #titulo de la ventana
ventana.geometry("300x200") #dimensiones de la ventana
ventana.configure(background= 'dark turquoise') #color de fondo de la ventana
var=tk.StringVar()

e1=tk.Label(ventana,text="Introduce la cantidad de bitcoin: ",bg="pink",fg="black") #etiqueta1
e1.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X) #posicionamiento de la etiqueta1
entrada1=tk.Entry(ventana) #caja de texto 1
entrada1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X) #posicionamiento de la caja de texto 1

e2=tk.Label(ventana,text="Introduce el valor de bitcoin en euros: ",bg="pink",fg="black") #etiqueta2
e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X) #posicionamiento de la etiqueta2
entrada2=tk.Entry(ventana) #caja de texto 2
entrada2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X) #posicionamiento de la caja de texto 2

botonMultiplicacion=tk.Button(ventana,text="Multiplicacion",command=multiplicacion) #boton de multiplicacion
botonMultiplicacion.pack(side=tk.TOP) #posicionamiento del boton de multiplicacion

res=tk.Label(ventana,textvariable=var,bg="plum",padx=5,pady=5,width=50) #etiqueta de resultado
res.pack() #posicionamiento de la etiqueta de resultado

botonCierra=tk.Button(ventana,text="Cerrar",fg="blue",command=cerrar) #boton de cerrar
botonCierra.pack(side=tk.TOP) #posicionamiento del boton de cerrar

ventana.mainloop()