import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

# Создание и запуск двух потоков на основе класса Knight
knight1 = Knight("Ланселот", 10)
knight2 = Knight("Галахад", 15)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Битвы окончены!")