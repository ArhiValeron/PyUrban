# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
#

calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string1):
    count_calls()
    return len(string1), string1.upper(), string1.lower()


def str_matches(string, list_to_search):
    count_calls()
    result_list = [string]
    for i in list_to_search:
        if string.lower() == i.lower():
            result_list += ["~", i]
    if result_list == [string]:
        result_list = ["No matches"]
    return result_list


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False


print(*string_info('London is the capital of Great Britain'))
print(*string_info('Armageddon is coming soon'))
print(is_contains('iS', ['ban', 'BaNaN', 'urBAN', "soon", "is", "Is"]))
print(is_contains('cycle', ['recycling', 'cyclic', "medic", "apple", "hole", "deer"]))
print(*str_matches('iS', ['ban', 'BaNaN', 'urBAN', "soon", "is", "Is"]))
print(*str_matches('cycle', ['recycling', 'cyclic', "medic", "apple", "hole", "deer"]))
print(calls)
