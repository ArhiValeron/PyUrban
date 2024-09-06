"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
 strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
 а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
"""

import os

def custom_write(file_name, strings):
    """
    Записывает строки в файл и возвращает словарь с позициями строк.

    Args:
    file_name: Имя файла для записи.
    strings: Список строк для записи.

    Returns:
    Словарь, где ключ - это кортеж (индекс строки, позиция в файле), а значение - строка.
    """
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as file: # использую функцию whit для того что бы не следить, когда закрыть файл.
          pass # закрываем файл созданный файл.

    with open(file_name, 'a', encoding='utf-8') as file:
        result = {}
        for index, string in enumerate(strings, 1):
            result.update({(index, file.tell()): string})
            file.write(string + '\n')
    return result




#############################################################################
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)