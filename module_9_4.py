first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))
"""
Результатом должен быть список совпадения букв в той же позиции:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.
"""


#################################################################
def get_advanced_writer(file_name):
    """
    :param file_name: название файла для записи
    :return: возвращает функцию write_everything
    """
    def write_everything(*data_set):
        """
        Производит запись в файл неограниченное количество переменных,
        :param data_set: замкнутый параметр с именем файла из родительской функции
        :return: функция не возвращает ничего
        """
        with open(file_name, "a", encoding="utf-8") as file:
            for item in data_set:
                file.write(f"\n {item}")
        return
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#################################################################

from random import choice

class MysticBall:
  def __init__(self, *words):
    self.words = list(words)

  def __call__(self):
    return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
