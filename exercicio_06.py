# 5 notas e media

notas = []

for i in range(5):

    nota = float(input(f'Digite a {i + 1}ª nota: '))

    notas.append(nota)

media = sum(notas) / len(notas)

acima_media = [n for n in notas if n > media]

print('A media é: ', media)

print('As notas acima da media são: ', acima_media)
