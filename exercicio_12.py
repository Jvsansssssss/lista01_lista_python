nomes = []

while True:

    print('1. Adicionar nome')

    print('2. Verificar se algum nome está na lista')

    print('3. Verificar quantidades de nomes na lista')

    print('4. Parar')

    print('')

    opcao = int(input('Escolha o numero de sua opção: '))

    if opcao == 1:

        print('')

        nome = input('Fale o nome para ser adicionado na lista: ')

        print('')

        print(f'{nome} foi adicionado na lista! ')

        print('')

        nomes.append(nome)

    if opcao == 2:
        print('')

        ver_nome = input('fale o nome quer você quer ver se tem na lista: ')

        print('')

        if ver_nome in nomes:

            print('')

            print(f'O nome {ver_nome}, está na lista!')

            print('')

        else:
            print('')

            print(f'O nome {ver_nome}, não está na lista!')

            print('')

    if opcao == 3:

        print('')

        print(f'A quantidade de nomes na lista é de: {len(nomes)} nomes')

        print('')

    if opcao == 4:

        print('')

        print('Parando o programa...')

        break

    if opcao > 4:

        print('')

        print('Opção invalida, tente novamente')

        print('')
