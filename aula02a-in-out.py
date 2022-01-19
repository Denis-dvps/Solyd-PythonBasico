name = input('Full Name: ')
age = int(input('Age: '))
height = float(input('Height: '))
typenam = type(name)
typeage = type(age)
typehei = type(height)
print(name, typenam)
print(age, typeage)
print(height, typehei)

# Concatenando com ','
print(name, 'has', age, 'years old and', height, 'tall.')

# Concatenando com o '+'
# print(name + ' has ' + str(age) + ' years old and ' + str(height) + ' tall.')
