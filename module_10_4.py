
import threading
from random import randint as rand
from time import sleep as sleep
from queue import Queue

class Table:
    def __init__(self,number, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.table = None
    def run(self):
        wait_time = rand(3, 10)
        print(f"{self.name} сидит за столом {self.table}, {wait_time} секунд.")
        sleep(wait_time)
        print(f"Гость {self.name} освободил стол {self.table} ")
        self.table = None


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def discuss_guests(self):
        while not self.queue.empty():
            guest = self.queue.get()
            guest_not_seated = True
            while guest_not_seated:
                for table in self.tables:
                    if table.guest == None or not table.guest.is_alive():
                        table.guest = guest
                        guest.table = table.number
                        guest.start()
                        guest_not_seated = False
                        break



    def guest_arrival(self, *guests):
        for guest in guests:
            self.queue.put(guest)
            print(f"{guest.name} в очереди")
        self.discuss_guests() # Функция старта обслуживания гостей перенесена в функцию приема гостей,
            # т.к. раз приперлись все равно обслуживать.





# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)


