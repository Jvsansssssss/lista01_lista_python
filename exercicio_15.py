# Faça um programa que simule uma lista de compras

lista_itens = []

while True:

    print('1. Adicionar item')

    print('2. Remover item')

    print('3. Mostrar lista')

    print('4. Sair')

    print('')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:

        item = input('Fale um item para adicionar na lista: ')

        lista_itens.append(item)

    if opcao == 2:

        removido = input('Fale um item para remover na lista: ')

        lista_itens.remove(removido)

    if opcao == 3:

        print('Lista:', lista_itens)

    if opcao == 4:

        print('Saindo...')

        break

    if opcao > 4:
        print('Opção invalida! ')
