# Напишите программу, которая запрашивает строку до тех пор, пока пользователь не введет “хватит”.
# Т.е. программа запрашивает ввод, если вводится любое значение отличное от слова “хватит”,
# то программа запрашивает ввод снова.

STOPKEY = 'хватит'
cmd = None

while cmd != STOPKEY:
    cmd = input('Input "' + STOPKEY + '": ')
