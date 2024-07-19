palavras = ('Python', 'Pedro', 'Vogais', 'Amo')

for palavra in palavras:
    print(f'A Palavra {palavra}, tem esse vogais: ')
    for letra in palavra:
            if letra.lower() in 'aeiou':
                print(f'A Palavra {palavra}, tem essas vogais: {letra}', end=' ')