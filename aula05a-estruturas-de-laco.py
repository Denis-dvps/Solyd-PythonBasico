names = ['Porsche', 'Lamborguini', 'Dodge', 'Maverick']
print(names)
print(names[0])

for name in names:
    print(name)

list_of_numbers = range(5, 11) # o último termo não é contabilizado, para que seja é necessário incluir +1, ou seja, para aparecer o 10, coloque 11
for item in list_of_numbers:
    print(item)

list_of_numbers = range(0, 100, 2) # o 2 é o passo, 2 em 2.
for item in list_of_numbers:
    print(item)

# abreviando
for i in range(0, 100, 2):
    print(i)

for i in range(len(names)):
    print(names[i])
    names.append('New') # adiciona nova entrada a lista, para cada entrada do for
print(names)