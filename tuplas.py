my_tuple = ("oi", "python")


# Uma vez que as tuplas são criadas, nós não podemos mudar os seus itens
foods = ("apple", "banana", "cherry")
foods2 = list(foods)
foods2[1] = "kiwi"
foods = tuple(foods2)

# Adicione Itens
# Converta a tupla em lita
comidas = ("maniçoba", "açaí")
comidas2 = list(comidas)
comidas2.append("arroz")
novas_comidas = tuple(comidas2)

# Adicione tuplas em tuplas
frutas = ("apple", "banana", "cherry")
frutas2 = ("orange",)
frutas += frutas2

