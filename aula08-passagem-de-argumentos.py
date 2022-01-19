import sys

arguments = sys.argv #arg1 metod // arg2 - n1 // arg3 - n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if arguments[1] == 'soma':
    result = soma(float(arguments[2]), float(arguments[3]))
elif arguments[1] == 'sub':
    result = sub(float(arguments[2]), float(arguments[3]))
print(result)
