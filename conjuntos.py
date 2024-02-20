conjunto = {"apple", "banana", "cherry"}


# Acesse os itens
# Não podemos acessar os itens através de indexes
# Podemos acessar os itens através de iterações
names = {"Giovanna", "Andreia", "Eduardo"}
for name in names:
    if "Giovanna" in names:
        print("Hello")

print("Giovanna" in names)

# Depois que o set é criado não podemos mudar um elemento, mas podemos
# adicionar mais elementos
names = {"Giovanna", "Andreia", "Eduardo"}
names.add("Maria")

# Update
names = {"Giovanna", "Andreia", "Eduardo"}
colors = {"azul", "verde", "amarelo"}
names.update(colors)

# Remova Itens
# Remove
names = {"Giovanna", "Andreia", "Eduardo"}
names.remove("Giovanna")

# Discard
names = {"Giovanna", "Andreia", "Eduardo"}
names.discard("Giovanna")

# Pop - Remove um item aleatório
names = {"Giovanna", "Andreia", "Eduardo"}
names.pop()

# Del - Deleta o conjunto inteiro
names = {"Giovanna", "Andreia", "Eduardo"}
del names

# Iteração
names = {"Giovanna", "Andreia", "Eduardo"}
for name in names:
    print(name)


# junte os conjuntos
# union()
names = {"Giovanna", "Andreia", "Eduardo"}
colors = {"azul", "verde", "amarelo"}
novo_conjunto = names.union(colors)

# update()
names = {"Giovanna", "Andreia", "Eduardo"}
colors = {"azul", "verde", "amarelo"}
names.update(colors)

# intersection_update() - Mantenha os itens que existe nos dois conjuntos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

# intersection() - Cria um novo set com itens que existem nos dois conjuntos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
c = {"google", "microsoft", "apple"}
z = x.intersection(y)
