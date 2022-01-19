'''Escreva uma função que recebe um objeto de coleção (lista, tupla, conjunto, dicionário)
e retorna o valor do maior número dentro dessa colecao. Faça outra função que retorna o menor número dessa coleção.'''


# MAIOR
def collect_max(n1, n2, n3, n4):
    list = [n1, n2, n3, n4]
    bigger = max(list)
    return bigger


# list2 = collection(1, 2, 3, 4)
# print(list2)

# MENOR
def collect_min(n1, n2, n3, n4):
    list = [n1, n2, n3, n4]
    smaller = min(list)
    return smaller

n1 = int(input('Insert the first number: '))
n2 = int(input('Insert the second number: '))
n3 = int(input('Insert the third number: '))
n4 = int(input('Inset the forth number: '))
max = collect_max(n1, n2, n3, n4)
min = collect_min(n1, n2, n3, n4)
print(f'The highest number is: {max}')
print(f'The smallest number is: {min}')
