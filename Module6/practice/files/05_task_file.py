# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день

import os

path = os.path.join('data', 'items_sold.txt')
with open(path, 'r', encoding='UTF-8') as f:
    sales = {}
    total_sum = 0
    for line in f:
        for sale in line.split():
            good, price = sale.split(':')
            prices = sales.setdefault(good, [])
            prices.append(float(price))
            total_sum += float(price)

print('1. Какова общая выручка магазина?')
print(f'   {total_sum:.2f}')

print('2. Какова выручка магазина по каждому типу товаров?')
for good, prices in sales.items():
    print(f'   {good:11}: {sum(prices):.2f}')

print('3. Какой тип товара был продан на самую большую сумму?')
max_price_sale = max(sales.items(), key=lambda x: x[-1])
print(f'   {max_price_sale[0]}')

print('4. Сколько различных типов товаров было продано за день?')
print(f'   {len(sales)}')
