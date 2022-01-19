phrase = 'oi, tudo bem?'
list_names = ['João', 'Laurinda', 'José', 'Laurentina']
print(phrase[12])
print(list_names[0])

# para imprimir o último ou de trás pra frente
print(list_names[-1:-5:-1])
print(list_names[-1:-5:-2])
print(list_names[-2:-5:-2])
print(list_names[-3:-5:-1])
print(list_names[-4:-5:-1])

list_names.append('Sebastião')
list_names.append('Ilza')
# list_names.remove() -> remove uma entrada da lista
# list_names.clear() -> limpa a lista
# list_names.insert(posição, 'texto')
# list_names.pop() -> printa o último e remove da lista
print(list_names)

phrase_new = phrase + ' Como vai você?'
print(phrase_new)
