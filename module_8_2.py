def personal_sum(numbers):
  """
  Функция подсчитывает сумму чисел в коллекции numbers.
    numbers: Коллекция чисел.
    Кортеж (result, incorrect_data), где:
      result - сумма чисел.
      incorrect_data - количество некорректных данных.
  """
  result = 0
  incorrect_data = 0
  for num in numbers:
    try:
      result += num
    except TypeError:
      incorrect_data += 1
  return result, incorrect_data


def calculate_average(numbers):
  """
  Функция вычисляет среднее арифметическое чисел в коллекции numbers.
  Args:
    numbers: Коллекция чисел.
  Returns:
    Среднее арифметическое всех чисел в коллекции.
    Возвращает 0, если коллекция пуста или содержит только нечисловые элементы.
    Возвращает None, если в numbers записан некорректный тип данных.
  """
  try:
    sum, incorrect_data = personal_sum(numbers)
    if incorrect_data == len(numbers):
      return 0
    return sum / len(numbers)
  except ZeroDivisionError:
    return 0
  except TypeError:
    print('В numbers записан некорректный тип данных')
    return None


# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать