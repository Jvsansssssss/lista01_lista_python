# segundo maior sem sort

numeros = [7, 2, 9, 5, 3, 8]

maior = max(numeros)
numeros.remove(maior)
segundo_maior = max(numeros)

print("Segundo maior número:", segundo_maior)
