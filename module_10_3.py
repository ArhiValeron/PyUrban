import threading
import random
import time



class Bank:
    """
    Атрибуты объекта:
        balance - баланс банка (int)
        lock - объект класса Lock для блокировки потоков.
    Методы объекта:
        Метод deposit:
            Будет совершать 100 транзакций пополнения средств.
            Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
            Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
            После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
            Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
        Метод take:
            Будет совершать 100 транзакций снятия.
            Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
            В начале должно выводится сообщение "Запрос на <случайное число>".
            Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
            Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.
    """
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            self.lock.acquire()
            if self.balance >= 500 and self.lock.locked():
                print("Больше 500")# Проверяю баланс перед пополнением.
                self.lock.release()
                time.sleep(0.001)# Тут сбалансировал, что бы сразу не крутил цикл
                continue# Разблокировка, если баланс достиг 500 и замок заблокирован

            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)
            self.lock.release()  # разблокировка после каждой транзакции



    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            self.lock.acquire()
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)
            self.lock.release() # разблокировка после каждой транзакции





bank = Bank()

# Создание потоков
deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)

# Запуск потоков
deposit_thread.start()
take_thread.start()
deposit_thread.join()
take_thread.join()

