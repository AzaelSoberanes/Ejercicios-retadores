#Ejercicio Retador 2

municipios = []
habitantes = []
sumatoria_habitantes = 0

lista_municipios = input ("Ingresa un municipio: ")
municipios.append(lista_municipios)

lista_habitantes = int(input ("Ingresa numero de habitantes: "))
habitantes.append(lista_habitantes)

lista_municipios = input ("Ingresa un municipio: ")
municipios.append(lista_municipios)

lista_habitantes = int(input ("Ingresa numero de habitantes: "))
habitantes.append(lista_habitantes)

lista_municipios = input ("Ingresa un municipio: ")
municipios.append(lista_municipios)

lista_habitantes = int(input ("Ingresa numero de habitantes: "))
habitantes.append(lista_habitantes)

sumatoria_habitantes = sum(habitantes)
promedio_habitantes = sumatoria_habitantes/3

print("La suma total de habitantes es: " +str(sumatoria_habitantes))
print("El promedio de habitantes en los municipios es: " +str(promedio_habitantes))