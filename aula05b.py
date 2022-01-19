# Uma String também é um coleção
word = 'Denis dos Santos Lima'
for letter in word:
    print(letter)
# cada caractere numa string é um item.

i = 0
while i < 10: # enquanto essa condição for verdadeira irá entrar no while, quando for falsa irá sair
    print('i ainda é menor que 10: ', i)
    i = i + 1 # ou pode ser escrito como i += 1

print('Acabou o while pois i = a', i)

num = 0

while True:
    print(num)
    if num == 20:
        break
    num += 1
