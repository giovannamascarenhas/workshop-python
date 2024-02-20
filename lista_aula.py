# sintaxe
lista1 = [1,2, "python", True, [4,5,6], {'a': 1}]

lista2 = list((1,2,3))
# print(lista2)

# Converter string em lista
my_name = "Giovanna.Mascarenhas_hanahsbdbdbnd"
list(my_name)
# Converter listas em string 2
# print(my_name.split('.'))
new_lista = my_name.split('.')
# print(new_lista)

fruits = ["banana", "maçã", "banana", "uvas"]
fruits[0]
# primeiro elemento
# print(fruits[0])
# ultimo elemento
# print(fruits[-1])
# range + len()
# len() - quantos elementos existem na lista
for index in range(len(fruits)):
    index2 = fruits[index]


# num = 28
# num_str = str(num)
# num_list = list(num_str)
# print([int(index) for index in num_list])
# print()


# print(int(num_str))

# print(type(''.join(num_str)))


fruits = [
    "banana", 
    "maçã", 
    "banana", 
    "bacuri", 
    "melancia", 
    "cupuaçu", 
    "açaí", 
]
# slice
# print(fruits[1:4])
# for fruit in fruits:
#     if fruit == "bacuri":
#         print("Achou bacuri ", fruit)
have_bacuri = "bacuri" in fruits


fruits = [
    "banana", 
    "maçã", 
    "banana", 
    "bacuri", 
    "melancia", 
    "cupuaçu", 
    "açaí", 
]
# fruits[0] = "morango"
# fruits[1:3] = ["bacaba", "ameixa"]

# for fruit in range(len(fruits)):
#     if fruits[fruit] == "banana":
#         fruits[fruit] = "caju"
#         break
# print(fruits)

fruits = [
    "banana", 
    "maçã", 
    "banana", 
    "bacuri", 
    "melancia", 
    "cupuaçu", 
    "açaí", 
]
# fruits.insert(0, 'uvas')
# fruits.append('uvas')

# print(fruits)

lista_compras = [
    'arroz',
    'carne',
    'salada',
    'feijão'
]

# lista_compras.append('azeite')
# lista_compras.append('feijão')
# Adicionar vários elementos
# lista_compras.extend(('azeite', 'feijão'))
# print(lista_compras)

# lista_compras.remove('arroz')
# print(lista_compras)

# for elemento in lista_compras:
#     # if elemento == "arroz" or elemento == "feijão"
#     if elemento == "arroz":
#         lista_compras.remove(elemento)
#     elif elemento == "feijão":
#         lista_compras.remove(elemento)

# print("depois")
# print()
# print(lista_compras)
# del lista_compras
# lista_compras.clear()
# print(lista_compras)
# tem_arroz = "arroz" in lista_compras


# contador = 0
# while contador < len(lista_compras):
#     print(lista_compras[contador])
#     contador += 1

# Forma 1
copia_lista_compras = lista_compras.copy()
copia_lista_compras_2 = list(lista_compras)
copia_lista_compras_2.append('ovos')
# print('cópia: ', copia_lista_compras_2)
# print('original: ', lista_compras)

lista_compras = [
    'arroz',
    'carne',
    'salada',
    'feijão'
]
novos_elementos = ['ovos', 'sumos']
# lista_compras.extend(novos_elementos)
lista_compras.append(novos_elementos)
# print(lista_compras)
# for elemento in lista_compras:
#     # print(elemento)
#     # if type(elemento) == list
#     if isinstance(elemento, tuple):
#         for ele in elemento:
#             print(ele)

# listas = [[1,2], [3,4]]
# for ele in listas:
#     for element in ele:
#         print(element)


# Converta uma lista de string inteiros 
list = ['1', '2']
s = [str(i) for i in list]
print(s)
s = int("".join(s))
print(s)