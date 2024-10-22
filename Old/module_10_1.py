import time
from time import sleep

start_time = time.time()
def write_words(word_count, file_name):
    """
    Записывает слова в файл с заданным именем.

    Args:
        word_count (int): Количество записываемых слов.
        file_name (str): Имя файла.
    """

    with open(file_name, 'w', encoding = "UTF-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

# Вызов функции для записи слов в файлы
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_1 = time.time()
execution_time = time_1 - start_time
print(f"Время выполнения функций: {execution_time} секунд")


# Мультипоток
import threading

# Создание потоков для записи слов в файлы
threads = []
threads.append(threading.Thread(target=write_words, args=(10, "example5.txt")))
threads.append(threading.Thread(target=write_words, args=(30, "example6.txt")))
threads.append(threading.Thread(target=write_words, args=(200, "example7.txt")))
threads.append(threading.Thread(target=write_words, args=(100, "example8.txt")))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time = time.time()
execution_time = end_time - time_1

print(f"Время выполнения потоков: {execution_time} секунд")
