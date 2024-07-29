# Задача "Developer - не только разработчик":
# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте
# им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.


class House:
    def __init__(self, name, floors):
        self.number_of_floors = floors
        self.name = name

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(f"{i + 1} этаж")
        else:
            print(f"Такого этажа не существует")

    def __str__(self):
        return (f"Название: {self.name}, количество этажей: {self.number_of_floors}")

    def __len__(self):
        return self.number_of_floors

if __name__ == "__main__":
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    print(h1.name)
    h1.go_to(5)
    print(h2.name)
    h2.go_to(10)
