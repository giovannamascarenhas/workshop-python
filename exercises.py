# Escreva uma função que receba uma string como entrada e retorne o número de vogais que existe na palavra
# Escreva uma função que receba uma lista como entrada e retorne uma nova lista com os elementos invertidos.
# Escreva uma função que receba uma lista como entrada e retorne uma nova lista contendo apenas os elementos únicos da lista original, sem duplicatas.
# Escreva uma função que receba uma string como entrada e verifique se ela é um palíndromo (ou seja, se ela é a mesma quando lida da esquerda para a direita e da direita para a esquerda).

vogais = 'aeiouAEIOU'
palavra = 'ovos'

l = [1,2,3,4,5]
[5,4,3,2,1]

# List comp, tuple comp , dict comp
# lista1 = [1,2,3,4]
# # for num in lista1:
# #     print(num)

# # list comp
# print([num for num in lista1])

# # generator
# tuple = (num for num in lista1)
# for t in tuple:
#     print(t)
# # lista2 = []
# for num in lista1:
#     lista2.append(num*2)





def num_vogais(texto: str) -> int:
    vogais = 'aeiouAEIOU'
    num_vogais = 0
    for char in texto:
        if char in vogais:
            num_vogais += 1
    return num_vogais

texto = 'maria'
# print('Número de vogais: ', num_vogais(texto))

def return_nr_vogais(palavra: str) -> int:
    vogais =  'aeiouAEIOU'
    vogais = list(vogais)
    contador = 0
    print('aquiiii',palavra)
    for x in palavra:
        if x in vogais:
            contador += 1
    return print(contador)

# return_nr_vogais(texto)

vogais =  12

def reverter_lista(lista: list) -> list:
    # reverse
    # lista.reverse()
    # print(lista)
    # # return new_lista
    new_list = lista[::-1]
    # cópia da lista
    copia_lista = new_list[::]
    print(copia_lista)
    print(new_list)

l = [1,2,3,4,5]
print(reverter_lista(l))
