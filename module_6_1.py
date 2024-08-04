
"""
Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
 Метод eat(self, food): умертвит животное в случае не сьедобной пищи.
"""
class Animal:
    def eat(self, food):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.fed = False
                self.alive = False
    def __init__(self, name = 'Животное без имени', alive = True, fed= False):
        self.alive = alive
        self.fed = fed
        self.name = name

        


"""
Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
"""
class Plant():
    def __init__(self, edible = False, name = 'Растение без имени'):
        self.edible = edible
        self.name = name

"""
Mammal атрибут edible = True(съедобность), name - индивидуальное название каждого животного.
"""
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name = name)


"""
Класс Predator name - индивидуальное название каждого животного. Наследует Animal.
"""
class Predator(Animal):
    def __init__(self, name):
        super().__init__(name = name)

"""
Класс Flower name - индивидуальное название каждого растения. Наследует Plant.
"""
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name = name)

"""
Класс Fruit name - индивидуальное название каждого растения. Наследует Plant. edible = True(съедобность).
"""
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name = name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит') 
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
