palavra = 'palavra'

contador = ''

for i in palavra:
    contador += i

    print(contador)

for i in range(len(palavra)-2, 0, -1):
    print(palavra[:i])