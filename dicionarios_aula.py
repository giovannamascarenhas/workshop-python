# student  = {
#     "name": "João",
#     "age": 25,
#     "is_portuguese": True
# }
# student2 = dict(name="João", age=25, is_portuguese=True)
# new_dict = {
#     'key1': 'value',
#     'key2': {
#         'key3': 3
#     },
#     'key4': []
# }
# print('Nome: ', student2["name"])
# print("Number: ", student2.get("name"))


# print('Chaves: ', student2.keys())
# for key in student2.keys():
#     print(key)
# print("number" in student2.keys())

# for value in student.values():
#     print(value)
# print("João" in student.values())
# for key, value in student.items():
#     if key == 'name':
#         print(key)

# student  = {
#     "name": "João",
#     "age": 25,
#     "is_portuguese": True
# }
# student['number'] = 1234
# student['age'] = 30
# student.update({"address": "Rua 01"})
# print(student)

# Remove com a chave
# student.pop('address')
# Remove sem chave - remova o ultimo elemento
# student.popitem()

# del student["address"]
# print(student)

student  = {
    "name": "João",
    "age": 25,
    "is_portuguese": True
}

print("João" in student.values())
# print(student)
# for value in student:
#     print(student[value])

# for key, value in student.items():
#     print(f"{key} -> {value}")