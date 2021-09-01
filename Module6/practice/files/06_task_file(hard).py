# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

staff = {}

path = os.path.join('data', 'workers.txt')
with open(path, 'r', encoding='UTF-8') as f:
    f.readline()
    for line in f:
        fname, lname, salary, position, norm = line.split()
        staff[fname + ' ' + lname] = {
            'rate': int(salary) / int(norm),
            'norm': int(norm),
            'hours': 0,
            'pay': 0
        }

path = os.path.join('data', 'hours_of.txt')
with open(path, 'r', encoding='UTF-8') as f:
    f.readline()
    for line in f:
        fname, lname, hours = line.split()
        emp = staff.setdefault(fname + ' ' + lname, {
            'rate': 0,
            'norm': 0
        })
        emp['hours'] = int(hours)
        if emp['hours'] <= emp['norm']:
            emp['pay'] = emp['rate'] * emp['hours']
        else:
            emp['pay'] = emp['rate'] * (2 * emp['hours'] - emp['norm'])

for emp, data in staff.items():
    print(f"{emp:20} {data['pay']:.2f}")
