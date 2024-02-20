student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
}

# Chave
# Uma chave no dicionário não pode ser repetido
print(student["age"])
print(student.get("name", None))

# Len
print(len(student))

# construtor dict
student2 = dict(name="Giovanna", age=28)
print(student2)


# Acessar Itens
print(student["age"])
print(student.get("name", None))
# Mostre a lista de chaves
print(student.keys())
# Mostre os itens
print(student.values())
# Mostre os itens
print(student.items())


# Mudar valores
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
}
student["school"] = "A nice school"

# Update()
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
}
student.update({"school": "A nice school"})

# Remove - pop() - Precisamos passar a key
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
  "school": "A nice school"
}
student.pop("is_portuguese")

# Remove - popitem() - remove o último item
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
  "school": "A nice school"
}
student.popitem()

# Remove - del - Precisamos passar a key
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
  "school": "A nice school"
}
del student["name"]

# Clear
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
  "school": "A nice school"
}
student.clear()


# Iterações
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
  "school": "A nice school"
}
for value in student:
    print(value)

for key, value in student.items():
    print(key, value)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)


# Copy
student = {
  "name": "Afonso",
  "age": 26,
  "is_portuguese": True,
  "school": "A nice school"
}
student_copy = student.copy()
