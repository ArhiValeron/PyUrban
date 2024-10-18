import threading
import random
import time
import queue

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.task_queue = queue.Queue()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.task_queue.put(('deposit', amount))
            time.sleep(0.01)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.task_queue.put(('take', amount))
            time.sleep(0.01)

    def process_task(self):
        while True:
            task, amount = self.task_queue.get()
            self.lock.acquire()
            try:
                if task == 'deposit':
                    self.balance += amount
                    print(f"Пополнение: {amount}. Баланс: {self.balance}")
                elif task == 'take':
                    if amount <= self.balance:
                        self.balance -= amount
                        print(f"Снятие: {amount}. Баланс: {self.balance}")
                    else:
                        print("Запрос отклонён, недостаточно средств")
            finally:
                self.lock.release()
            self.task_queue.task_done()

# Создание объекта Bank
bank = Bank()

# Создание потоков
deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)
process_thread = threading.Thread(target=bank.process_task)

# Запуск потоков
deposit_thread.start()
take_thread.start()
process_thread.start()

# Ожидание завершения потоков
deposit_thread.join()
take_thread.join()
process_thread.join()
