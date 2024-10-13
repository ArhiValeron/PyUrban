class IncorrectVinNumber(Exception):
    """Исключение для некорректного VIN номера."""

    def __init__(self, message="Некорректный VIN номер"):
        super().__init__(message)
        self.message = message


class IncorrectCarNumbers(Exception):
    """Исключение для некорректных номеров автомобиля."""

    def __init__(self, message="Некорректные номера автомобиля"):
        super().__init__(message)
        self.message = message


class Car:
    """Класс для представления автомобиля."""

    def __init__(self, model, vin, numbers):
        """Инициализация объекта Car.
        Args:
        model: Название модели автомобиля.
        vin: VIN номер автомобиля (1000000-9999999).
        numbers: Номера автомобиля(6 символов).
        """
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):

        """Проверка корректности VIN номера.
        Args:
        vin_number: VIN номер для проверки.
        Returns:
        True, если VIN номер корректен.
        Raises:
        IncorrectVinNumber: Если VIN номер некорректен.
        """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номера")
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers):
        """Проверка корректности номеров автомобиля.
        Args:
        numbers: Номера автомобиля для проверки.
        Returns:
        True, если номера автомобиля корректны.
        Raises:
        IncorrectCarNumbers: Если номера автомобиля некорректны.
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True


##################################################
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
