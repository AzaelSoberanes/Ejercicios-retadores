#ejercicio integrador 1


maiz_grano = ["Maiz grano", 285.55]
pepino = ["Pepino", 334.72]
tomate_verde = ["Tomate verde", 129.00]
ventas_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]]




producto = str(input("Id del producto: "))
numero_cajas = int(input("Numero de cajas a vender: "))

if producto == str(1):
  print("El producto es: "+maiz_grano[0])
  print("El precio por caja es: "+str(maiz_grano[1]))
  suma = numero_cajas*maiz_grano[1]
  if numero_cajas<=100:
    suma += 1500

  
if producto == str(2):
  print("El producto es: "+pepino[0])
  print("El precio por caja es: "+str(pepino[1]))
  suma = numero_cajas*pepino[1]
  if numero_cajas<=100:
    suma += 1500
  
  
if producto == str(3):
  print("El producto es: "+tomate_verde[0])
  print("El precio por caja es: "+str(tomate_verde[1]))
  suma = numero_cajas*tomate_verde[1]
  if numero_cajas<=100:
    suma += 1500
  
if producto > str(3):
  print("Opcion no valida")


ventas = ventas_productos[0][1]+ ventas_productos[1][1]+ ventas_productos[2][1]+ ventas_productos[3][1]+ventas_productos[4][1]+ventas_productos[5][1]+ventas_productos[6][1]+ventas_productos[7][1]+ventas_productos[8][1]+ventas_productos[9][1]

if ventas<1500:
  descuento = suma*.20
  suma -= descuento
  desc = True 
  print("Aplica descuento del 20%: "+str(desc))
  print("El total a pagar es: "+str(suma))