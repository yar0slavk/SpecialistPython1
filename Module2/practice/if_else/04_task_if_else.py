# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here

a = int(input('Input a: '))

if a % 15 == 0:
    print('Foobar')
elif a % 3 == 0:
    print('Foo')
elif a % 5 == 0:
    print('Bar')
