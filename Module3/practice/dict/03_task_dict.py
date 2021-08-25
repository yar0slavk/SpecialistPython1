# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 34500
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
# только один сотрудник
max_emp = max(staff, key=lambda emp: emp['salary'])
print(max_emp['name'], max_emp['surname'])
# все сотрудники
max_sal = max([emp['salary'] for emp in staff])
max_emp = [f"{emp['name']} {emp['surname']}" for emp in staff if emp['salary'] == max_sal]
print(f"({max_sal}) {', '.join(max_emp)}")
print()

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
# только один сотрудник
min_emp = min(staff, key=lambda emp: emp['salary'])
print(min_emp['name'], min_emp['surname'])
# все сотрудники
min_sal = min([emp['salary'] for emp in staff])
min_emp = [f"{emp['name']} {emp['surname']}" for emp in staff if emp['salary'] == min_sal]
print(f"({min_sal}) {', '.join(min_emp)}")
print()

print("Среднеарифметическую зарплату всех сотрудников")
salaries = [emp['salary'] for emp in staff]
print(sum(salaries) / len(salaries))
print()

print("Количество однофамильцев в организации")
surnames = [emp['surname'] for emp in staff]
namesakes = [sn for sn in surnames if surnames.count(sn) > 1]
print(len(namesakes))
print()

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
staff_sorted = sorted(staff, key=lambda emp: emp['salary'])
print('\n'.join([f"{emp['name']} {emp['surname']} ({emp['salary']})" for emp in staff_sorted]))
