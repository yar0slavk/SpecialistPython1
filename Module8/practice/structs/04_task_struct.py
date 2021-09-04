# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один
dictionary = dict(tuple(dictionary_1.items()) + tuple(dictionary_2.items()))
print(dictionary)

dictionary = {**dictionary_1, **dictionary_2}
print(dictionary)

dictionary = dictionary_1 | dictionary_2
print(dictionary)
