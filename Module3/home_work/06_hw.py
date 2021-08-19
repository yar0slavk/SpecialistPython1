# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

brands = [item['brand'] for item in items]
print(set(brands))

print("На складе больше всего товаров брэнда(ов): ")

max_count = brands.count(max(brands, key=brands.count))
print(set([brand for brand in brands if brands.count(brand) == max_count]))

print("На складе самый дорогой товар брэнда(ов): ")

max_price = max([item['price'] for item in items])
print(set([item['brand'] for item in items if item['price'] == max_price]))
