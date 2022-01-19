''' Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
Após isso irá imprimir todos os nomes da lista '''

invitednum = int(input('How many people you will invite? '))
#print(invitednum)
i = invitednum
listname = []
for guest in range(i):
     name = str(input('Insert guest name: '))
     listname.append(name)

print(listname)


#while i <= i:
#    g = str(input('Insert guest name: '))


