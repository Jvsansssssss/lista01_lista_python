# lista de produtos e preços

produtos = []

preco = []

while True:

    print('1. Adicionar produtos')

    print('2. Adicionar preço')

    print('3. Parar')

    print('')

    print('Observação: Após adicionar seu produto, adicione o preço!')

    print('')

    opcao = int(input("Fale o numero da opção desejada: "))

    if opcao == 1:

        produtinho = input('Fale um produto para adicionar a lista: ')

        produtos.append(produtinho)

    if opcao == 2:

        precinho = float(input('Fale o preço do produtinho: '))

        preco.append(precinho)

    if opcao == 3:
        print('Você parou de adicionar produtos e seus preços!')

        print(f'Você adicionou {len(produtos)} produtos e {len(preco)} preços')

        print('Os produtos adicionados foram: ', produtos)

        print('E seus respectivos preços são: ', preco)

        break

    else:
        print('Opção invalida!')
