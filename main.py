# 1. [x] Приветствие
# 2. [x] Мануал – как пользоваться программой и какие валюты доступны
# 3. [x] Ввести исходную валюту
# 4. [x] Ввести в какую валюту перевести
# 5. [x] Количество валюты
# 6. [x] Подсчёт
# 7. [x] Вывод результата

from converter import convert

# TODO: Использовать данные из АПИ
currencies = {
    'USD': 1,
    'RUB': 91.4,
    'EUR': 0.9,
}

print('Добро пожаловать в Конвертер Валют')
print('''
Инструкция:
1. Введите исходную валюту
2. Введите результирующую валюту
3. Введите количество исходной валюты

Доступные валюты:
''')

for currency in currencies.keys():
    print(f'- {currency} [{currencies[currency]}]')

original_currency = input('1. Введите исходную валюту: ')
result_currency = input('2. Введите результирующую валюту: ')
original_amount = input('3. Введите количество исходной валюты: ')

# TODO: Обрабатывать ошибки (несуществующая валюта + не числа в количестве)
# TODO: Обрабатывать не только целые числа
# NOTE: Как-то обрабатывать отрицательные числа
result_amount = convert(original_currency, result_currency, int(original_amount), currencies)

print(f'{original_amount} {original_currency} = {result_amount} {result_currency}')
