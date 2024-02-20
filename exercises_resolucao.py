def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador


texto = "Python é uma linguagem de programação"
print("Número de vogais:", contar_vogais(texto))

def inverter_lista(lista):
    return lista[::-1]


lista_original = [1, 2, 3, 4, 5]
print("Lista original:", lista_original)
print("Lista invertida:", inverter_lista(lista_original))


def remover_duplicatas(lista):
    return list(set(lista))

lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
print("Lista com duplicatas:", lista_com_duplicatas)
print("Lista sem duplicatas:", remover_duplicatas(lista_com_duplicatas))

def is_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


palavra1 = "ovo"
palavra2 = "python"
print("É 'ovo' um palíndromo?", is_palindromo(palavra1))
print("É 'python' um palíndromo?", is_palindromo(palavra2))

