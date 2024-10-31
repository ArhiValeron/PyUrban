import multiprocessing
from time import time as time


def read_info(name):
    all_data = []
    with open(name, "r", encoding="UTF-8") as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break
    return f"Файл {name} обработан."


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    Line_time_start = time()
    print("Начато линейное исполнение задачи:")
    # Линейный вызов
    for file in filenames:
        print(read_info(file))
    Line_time_stop = time()
    print(f"Линейное исполнение заняло {Line_time_start-Line_time_stop:.10f} секунд")

# Многопроцессный
    Multiproc_time_start = time()
    print("Начато многопроцессное исполнение задачи:")
    with multiprocessing.Pool(processes=4) as pool:
        print(pool.map(read_info, filenames))
    Multiproc_time_stop = time()
    print(f"Многопроцессное исполнение заняло {Multiproc_time_start-Multiproc_time_stop:.10f} секунд")