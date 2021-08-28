# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

path = os.path.join('data', 'fruits.txt')
f = open(path, 'r', encoding='UTF-8')
fruit_dict = {}
for line in f:
    fruit = line.rstrip()
    if not fruit:
        continue
    lst = fruit_dict.setdefault(fruit[0], [])
    lst.append(fruit)
f.close()

if len(fruit_dict):
    for letter, fruits in fruit_dict.items():
        filename = 'fruits_' + letter + '.txt'
        path = os.path.join('data', filename)
        f = open(path, 'w', encoding='UTF-8')
        for fruit in fruits:
            f.write(fruit + '\n')
        f.close()
