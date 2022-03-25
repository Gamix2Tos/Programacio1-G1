""" 
4.1 Implemente una tupla de un solo elemento. Tiene una particularidad, investigue. (2pts.)

4.2 Dada una lista de las edades de una población que ha ido a vacunarse,

vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]

Elimine de la lista, todas las ocurrencias del entero 10 (3pts)

Fecha tope de entrega: lunes 28 de Marzo. 4:30pm.
"""


#1 tupla de un solo elemento. Debe tener coma(,).
vlenguaje = ('Python',)



print(vlenguaje)

#2 Elimine de la lista, todas las ocurrencias del entero 10 (con "remove" se elimina la ocurrencia del valor.)
vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]
vdel = 10

for vocu in vEdades:
	if(vocu==vdel):
		vEdades.remove(vdel)
"""
otra opcion es por cada uno de los enteros 10 a eliminar pero seria poco practico si no conoces la cantidad.
vEdades.remove(10,)
vEdades.remove(10,)
vEdades.remove(10,)
vEdades.remove(10,)

"""


print("sin el 10",vEdades)
