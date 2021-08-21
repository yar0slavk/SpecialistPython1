# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def get_time(seconds):
    hh24 = seconds // 3600
    mi = (seconds - hh24 * 3600) // 60
    ss = seconds % 60
    return f'{hh24:0>2}:{mi:0>2}:{ss:0>2}'


print(get_time(29143))
print(get_time(13))
print(get_time(120))
print(get_time(3660))
