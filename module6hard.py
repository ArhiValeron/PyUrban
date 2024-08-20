from math import pi


"""
Класс Фигура: содержит базовые функции:
get_color(self):    # Возвращает цвет
set_color(self, r, g, b): # Устанавливает цвет
get_sides(self): # Возвращает список сторон
__len__(self): # Возвращает сумму всех сторон(периметр)
get_sides(self): # Возвращает список сторон

Сам по себе класс безполезен используется как родитель других классов фигур.
"""
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = [1] * self.sides_count if len(sides) != self.sides_count else list(sides)
        self.__color = color
        self.filled = True

    def get_color(self):    # Возвращает цвет
        return self.__color

    def __is_valid_color(self, r, g, b): # Возвращает True, если цвет введен корректно
        return all(0 <= value <= 255 and isinstance(value, int) for value in [r, g, b])

    def set_color(self, r, g, b): # Устанавливает цвет
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides): # Возвращает True, если все стороны введены корректно
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self): # Возвращает список сторон
        return self.__sides

    def __len__(self): # Возвращает сумму всех сторон(периметр)
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # Устанавливает значения сторон
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
"""
Класс Круг наследуется от класса Фигура Circle(Figure):
содержит функции:
get_square(self): # Возвращает площадь круга
также смотри функции родительского класса
"""
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figure__sides[0] / (2 * pi)  # Досуп к родителю

    def get_square(self): # Возвращает площадь круга
        return pi * self.__radius ** 2

"""
Класс Квадрат наследуется от класса Фигура Square(Figure):
содержит функции:
get_square(self): # Возвращает площадь треугольника
также смотри функции родительского класса
"""
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self): # Возвращает площадь треугольника
        s = sum(self._Figure__sides) / 2                # Досуп к родителю
        return (s * (s - self._Figure__sides[0]) * (s - self._Figure__sides[1]) * (s - self._Figure__sides[2])) ** 0.5

"""
Класс Куб наследуется от класса Фигура Cube(Figure):
содержит функции:
get_volume(self): # Возвращает объём куба
также смотри функции родительского класса
"""
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * 12
        super().__init__(color, *sides)

    def get_volume(self): # Возвращает объём куба
        return self._Figure__sides[0] ** 3


######################################################################

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
