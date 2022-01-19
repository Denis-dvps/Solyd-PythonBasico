my_list = ['Porsche', 'Lamborguini'] # list -> mutável.
my_tuple = ('Porsche', 'Lamborguini') # tuple -> Não mutável.
my_dictionary = {'nome': 'Denis', 'idade': 35} # dict - Sempre vai ter uma key 'nome' e uma value 'Denis', por exemplo. Mutável
my_set = {'Denis', 'Lima', 'Lima'} # Conjunto, itens repetidos só será mostrado um item daquele tipo. Mutável. Não ordenado.

'''O conjunto o dicionário para pesquisa é mais rápido que a lista'''

print(my_dictionary['idade'])
my_dictionary['endereco'] = 'Av. João das Neves'
my_dictionary['telefone'] = '99999-8888'
print(my_dictionary)
print(my_dictionary['idade'])

my_set.add('Maria')
my_set.remove('Lima')
print(my_set)
if 'Denis' in my_set: # é possível perguntar também se o item não está dentro com o "not in" da função
    print('Foi encontrado dentro do conjunto')

list = []
tuple = ()
my_dict = {} # ou dict()
my_set = set()

# É possível combinar os tipos de coleções
# ex.: uma lista com 4 tuplas, e dentro da última tupla dois dict.
combination = [(1, 2), (3, 4), (5, 6), ({'joao', 'maria'}, {'pedro'})]
print(combination)
