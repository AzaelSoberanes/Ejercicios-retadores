#Ejercicio retador 4
maiz_grano = ["Maiz grano", 285.55]
pepino = ["Pepino", 334.72]
tomate_verde = ["Tomate verde", 129.00]


producto = str(input("Id del producto: "))
numero_cajas = int(input("Numero de cajas a vender: "))

if producto == str(1):
  print("El producto es: "+maiz_grano[0])
  print("El precio por caja es: "+str(maiz_grano[1]))
  suma = numero_cajas*maiz_grano[1]
  print("El costo total a pagar es: "+str(suma))
if producto == str(2):
  print("El producto es: "+pepino[0])
  print("El precio por caja es: "+str(pepino[1]))
  suma = numero_cajas*pepino[1]
  print("El costo total a pagar es: "+str(suma))
if producto == str(3):
  print("El producto es: "+tomate_verde[0])
  print("El precio por caja es: "+str(tomate_verde[1]))
  suma = numero_cajas*tomate_verde[1]
  print("El costo total a pagar es: "+str(suma))
if producto > str(3):
  print("Opcion no valida")