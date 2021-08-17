# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

DAYS = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
        'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth',
        'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth',
        'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 'twenty-ninth', 'thirtieth', 'thirty-first')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December')

date = input('Input date (dd.mm.yyyy): ')
dd, mm, yyyy = date.split('.')
print(f'{DAYS[int(dd) - 1]} of {MONTHS[int(mm) - 1]}, {yyyy}')
