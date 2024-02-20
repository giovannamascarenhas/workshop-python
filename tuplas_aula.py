lista = [1,2,3]
lista[0] = 5

tupla = (1,2,3)
# tupla[0] = 5
# print()

foods = ('feijão', 'massa')
novo_elemento = "laranja"
foods_list = list(foods)
foods_list.append(novo_elemento)
foods_tuple = tuple(foods_list)
# print(f'Tipo: {type(foods_tuple)}, Foods: {foods_tuple}')

for food in range(len(foods_tuple)):
    print(foods_tuple[food])

# enumerate()
for index, value in enumerate(foods_tuple):
    print(f'{index} -> {value}')
