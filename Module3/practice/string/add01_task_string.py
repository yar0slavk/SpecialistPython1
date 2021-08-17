# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

LENGTH = 7
TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pla-erat consequat vestibulum. " \
       "Donec tincidunt sed lo-rem et feug-iat. Nullam eleme-ntum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

tmp_str = TEXT
punct = ('.', ',', '!', '?', '-')

for sign in punct:
    tmp_str = tmp_str.replace(sign, '')

num_words = 0
for word in tmp_str.split(' '):
    if len(word) > LENGTH:
        num_words += 1

print('number of words(len='+str(LENGTH)+'):', num_words)
