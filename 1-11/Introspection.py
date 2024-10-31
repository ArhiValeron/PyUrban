def introspection_info(obj):
  """
  Функция для интроспекции объекта.

  Args:
    obj: Объект, который нужно исследовать.

  Returns:
    Словарь с информацией об объекте.
  """

  info = {
      'type': type(obj).__name__,
      'attributes': dir(obj),
      'methods': [
          method_name for method_name in dir(obj) if callable(getattr(obj, method_name))
      ],
      'module': obj.__module__ if hasattr(obj, '__module__') else 'None',
  }

  # Дополнительные свойства для определенных типов объектов:
  if isinstance(obj, (list, tuple, set, dict)):
    info['length'] = len(obj)
  elif isinstance(obj, str):
    info['length'] = len(obj)
  elif isinstance(obj, (int, float, complex)):
    info['value'] = obj

  return info

class Testo:
    def __init__(self):
        TestoT = "TestO"
# Пример использования:
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello world!")
print(string_info)

list_info = introspection_info([1, 2, 3, 4])
print(list_info)

ABC = Testo()
list_info = introspection_info(ABC)
print(list_info)
