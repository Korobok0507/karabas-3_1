# Глобальная переменная.
calls = 0

# Функция счётчика вызово функций
def count_calls():
    global calls
    calls += 1

# Функция определения длины строки, перевода в верхний и нижний регистр
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция поиска строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    string_lower = string.lower()
    return any(item.lower() == string_lower for item in list_to_search)

# Вывод результатов
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))    # False

# Выводим количество вызовов функций
print(calls)