# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup1 = (1, 0, 7, 10, 10, 2, 4, -60, 0)
tup2 = (0, 6, 2, -4, -12, -6)
tup3 = (22, 41, -16, 3, 33, 19, 0, 2)

# num_of_common = 0
# for i, el in enumerate(tup1):
#     if el in tup2 and el in tup3 and i == tup1.index(el):
#         num_of_common += 1
# print('Number of common elements:', num_of_common)

print('Number of common elements:', len(set(tup1) & set(tup2) & set(tup3)))
