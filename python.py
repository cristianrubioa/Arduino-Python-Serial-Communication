# -*- encoding: UTF-8 -*-

import serial  #Biblioteca para establecer comunicacion Serial

SerialPort = serial.Serial('/dev/tty.wchusbserial1410', 9600)  #...Crea un objeto de puerto serie 

print SerialPort.readline() #Lee los datos(mensaje) enviados por Arduino y los imprime
print("Presione 1 para encender el Led y 0 para apagarlo ")

while 1:
    var = raw_input()  #...Espera hasta que el usuario ingrese los datos
    print "Ingresaste", var #Imprime los datos

    if(var == '1'): # Si los datos ingreados en var son 1
        SerialPort.write('1')  #Envia 1 a Arduino
        print("Led encendido")


    if(var == '0'): # Si los datos ingreados en var son 0
        SerialPort.write('0')  #Envia 0 a Arduino
        print("Led apagado")
