fruits = ["banana", "maçã", "banana", "uvas"]
indice = fruits[1]
ultimo_indice = fruits[-1]


# Len
fruits = ["banana", "maçã", "banana", "uvas"]
tamanho_lista = len(fruits)
random_list = [1,2, True, "Hello", 1.2]
new_list = list((1,2,3,4,5))


# Range of Indexes
fruits = [
    "banana", 
    "maçã", 
    "banana", 
    "bacuri", 
    "melancia", 
    "cupuaçu", 
    "açaí", 
]
fruits[1:4]
fruits[:-1]
# Copy of the list
new_fruits = fruits[:]

# Checar se item existe
# if "açaí" in fruits:
#     print("No estado do Pará comemos açaí com peixe frito")

# Mude um item da lista
fruits = ["bacuri", "cupuaçu", "açaí"]
fruits[0] = "bacaba"
fruits[1:3] = ["blackcurrant", "watermelon"]




# Insert
foods = ["maniçoba", "vatapá"]
foods.insert(1, "Pato no tucupí")

# Append
foods = ["maniçoba", "vatapá"]
foods.append("Peixe Frito")

# Extend
foods = ["maniçoba", "vatapá"]
foods.extend(["Pato no tucupí", "Tacacá"])


# Remove
foods = ["maniçoba", "vatapá"]
foods.remove("maniçoba")


# Pop - Elime o último item da lista
foods = ["maniçoba", "vatapá", "tacacá"]
foods.pop()

# Pop - Elime um item da lista passando o indice
foods = ["maniçoba", "vatapá", "tacacá"]
foods.pop(0)

# Del - Delete um item da lista
foods = ["maniçoba", "vatapá", "tacacá"]
del foods[0]

# Del - Delete a lista
foods = ["maniçoba", "vatapá", "tacacá"]
del foods


# Clear
foods = ["maniçoba", "vatapá", "tacacá"]
foods.clear()



# Loop
foods = ["maniçoba", "vatapá", "tacacá"]
for food in foods:
    print(food)

# Use o range juntamente com o len
foods = ["maniçoba", "vatapá", "tacacá"]
for food in range(len(foods)):
    print(f"{food} -> {foods[food]}")

# Enumerate
foods = ["maniçoba", "vatapá", "tacacá"]
for index, element in enumerate(foods):
    print(f"{index} -> {element}")

# While
foods = ["maniçoba", "vatapá", "tacacá"]
contador = 0
while contador < len(foods):
    print(foods[contador])
    contador += 1

# Sort
foods = ["maniçoba", "vatapá", "tacacá", "açaí"]
foods.sort()

# Sort - reverse
foods = ["maniçoba", "vatapá", "tacacá", "açaí"]
foods.sort(reverse=True)

# Copy
# Não podemos fazer cópias simplesmente fazendo lista1 = lista2
# Isso fará apenas uma referêcia
# Todas as mudanças feitas na lista1 serão aplicadas para a ista2
# Copy
foods = ["maniçoba", "vatapá", "tacacá", "açaí"]
foods2 = foods.copy()

# Outra maneira - list()
foods = ["maniçoba", "vatapá", "tacacá", "açaí"]
foods2 = list(foods)


# List Comprehension
foods = ["maniçoba", "vatapá", "tacacá"]
# print([food for food in foods])



# Join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2

# Join listas com apend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

# Join com extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)

