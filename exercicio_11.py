# 10 numeros

numeros = []

for i in range(10):

    numeroszinhos = float(input(f'Fale o {i + 1}º numero: '))

    numeros.append(numeroszinhos)

maior_que_dez = [n for n in numeros if n > 10]

print("A lista original:", numeros)

print('A lista com numeros maiores que dez:', maior_que_dez)
