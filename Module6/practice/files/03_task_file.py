# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)

f = open('data/salaries.txt', 'r', encoding='UTF-8')
f.readline()
staff = []
for line in f:
    emp = line.split()
    if int(emp[3]) > 60000:
        staff.append(f'{emp[0]} {emp[1][0]}.{emp[2][0]}')
f.close()

if len(staff):
    f = open('data/highly_paid.txt', 'w', encoding='UTF-8')
    for emp in staff:
        f.write(emp + '\n')
    f.close()
