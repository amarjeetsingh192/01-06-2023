dict_a = {"name": "raj","age": 25 }
dict_b = dict_a.copy()
dict_b["age"] = 30
print(dict_a)
print(dict_b)
print(id(dict_a))
print(id(dict_b))


# list_copy
list_a = ["raj",20]
list_b = list_a.copy()
print(list_a)
print(list_b)
print(id(list_a))
print(id(list_b))