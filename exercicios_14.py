# Peça ao usuário 5 nomes e os armazene em uma lista.

lista_nomes = []

for i in range(5):

    nome = input((f'Fale o {i + 1}º nome: '))

    lista_nomes.append(nome)

inversa = sorted(lista_nomes, reverse=True)

print('A Lista de nomes original:', lista_nomes)

print('A lista de nomes inversa:', inversa)
