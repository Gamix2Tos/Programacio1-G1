"""
Actividad Evaluada

1 Defina una función en python que acepte el radio y devuelva el valor del
area de un círculo de esas dimensiones. (4pts)

2 Defina una función en python que acepte 3 valores y devuelva solo el maximo
de los tres. (7pts)

3 Dado una lista de enteros, defina una función en python que devuelva la suma
de solo los valores impares de dicha lista. (7pts)

4 Desarrolle una función en python que acepte una variable string como primer
parámetro y la cantidad de caracteres de como segundo parámetro. La función
debe retornar un nuevo string que consista en el string original y el número
correcto de caracteres necesarios para que el string se salga centrado. 
No agregue caracteres al final del string. (10pts)

Fecha de Entrega: Lunes 16/05 """

# 1

from math import pi

def area_circulo(r):
	area = pi * r ** 2
	return area
r = area_circulo (float(input("coloque radio a usar:")))
print("el area del circulo es:", r)



# 2

def valor_maximo(valores):
    mayor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    return mayor


a = float(input("indique un numero:")),
b = float(input("indique un numero:")),
c = float(input("indique un numero:")),

numeros = a, b, c,
print("el numero mayor es:", (valor_maximo(numeros)))


# 3 Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista. (7pts)

def	Impar_detector(numeros):
	impares = []

	for n in numeros:
		if n % 2 == 1:
			impares.append(n)

	return impares
#lista_numeros = [1,2,3,4,5]
lista_numeros = list(range(1,21))
print("mi lista de numeros",lista_numeros)
filtro = Impar_detector(lista_numeros)
print("Numeros impares de la lista anterior",filtro)

"""
4 Desarrolle una función en python que acepte una variable string como primer
parámetro y la cantidad de caracteres de como segundo parámetro. La función
debe retornar un nuevo string que consista en el string original y el número
correcto de caracteres necesarios para que el string se salga centrado. 
No agregue caracteres al final del string. (10pts)"""

"""frase = 'programcion 1 ucla'
print(len(frase))
def centrar(s,n):
    """

"""texto= 'programacion'
print(format(texto, '^120'))
print(format(texto, '=^120'))
print(format(texto.rjust(58)))"""

def ContarCaracteres(vString):
    conteo = 0

    while vString[conteo:]:
        conteo +=1
    print("{:^120}".format(vString),'\n',"Cantidad de Caracteres del texto:",conteo)
    print("Cantidad de Caracteres necesarios para que salga centrado:", conteo^120)

    return conteo

ContarCaracteres(vString = input("Introduce texto :"))

#estaba con un amigo tratando de hacer este pero no lo logramos