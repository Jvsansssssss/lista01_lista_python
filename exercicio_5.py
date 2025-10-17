# lista com numeros pares e impares

lista_numeros = list(range(1, 11))

numeros_pares = [n for n in lista_numeros if n % 2 == 0]

numeros_impares = [n for n in lista_numeros if n % 2 != 0]

print('Os numeros pares são: ', numeros_pares)

print('Os numeros impares são: ', numeros_impares)
