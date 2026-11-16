from functools import partial

PRODUCTS = (
    {"name": "айфон 18 про макс", "category": "смартфон", "price": 1500},
    {"name": "айпад", "category": "планшет", "price": 1300},
    {"name": "макбук", "category": "ноутбук", "price": 3500},
    {"name": "самсунг галакси с26 ультра", "category": "смартфон", "price": 1350},
    {"name": "мси катана", "category": "ноутбук", "price": 2000},
)

NUMBERS = (3, 15, 7, 42, 0, 10, 99, -5)

# уровень 1
FILTER_BY = lambda key: lambda value: lambda items: (
    filter(lambda item: item[key] == value, items)
)


# уровень 2
UNCURRY_3 = lambda f: lambda a, b, c: f(a)(b)(c)

FILTER_BY_CATEGORY = partial(UNCURRY_3(FILTER_BY), "category")


# уровень 3
GREATER_THAN = lambda threshold: lambda x: x > threshold


print("Уровень 1:", list(FILTER_BY("category")("смартфон")(PRODUCTS)))
print("Уровень 2:", list(FILTER_BY_CATEGORY("ноутбук", PRODUCTS)))
print("Уровень 3:", list(filter(GREATER_THAN(10), NUMBERS)))
