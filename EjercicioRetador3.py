#ejercicio retador 3
#inicializamos variables
maximo = 3254
cincuenta_porciento = 1627
peso_costal_cemento = 40
peso_costal_yeso = 30


#pedimos la cantidad de costales al usuario
numero_costales_cemento = input("Ingrese el numero de costales de cemento: ")
peso_cemento = int(numero_costales_cemento)*peso_costal_cemento

numero_costales_yeso = input("Ingrese el numero de costales de yeso: ")
peso_yeso = int(numero_costales_yeso)*peso_costal_yeso
#se suma el peso de los costales de cemento y yeso
suma_pesos = peso_cemento+peso_yeso


if suma_pesos < cincuenta_porciento:
  si = False
else:
  if suma_pesos > maximo:
    si = False
  else:
    si = True
    
print("El peso total en Kg es: "+str(suma_pesos))
print("¿Se puede realizar el envio? " +str(si))