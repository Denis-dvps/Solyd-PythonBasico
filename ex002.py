'''Exercício:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exercito é preciso ter mais de 18 anos pesar mais ou igual a 60kg e medir mais ou igual a 1,70 metros
'''
age = int(input('Insert your age: '))
wei = float(input('Insert your weight: '))
hei = float(input('Insert your height: '))
if (age > 18) and (wei >= 60) and (hei >= 1.70):
    print('Ready to enter to the Army Forces')
else:
    print('Not ready to the Army Forces')
