# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)

HomeWorksDone = 12
TimeSpent = 1.5
CourseName = "Python"
AvTime = TimeSpent / HomeWorksDone

# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

print("Курс:", CourseName, "всего задач:", str(HomeWorksDone)+",", "затрачено часов: ",
      str(TimeSpent)+",", "среднее время выполнения ", AvTime, "часа")
