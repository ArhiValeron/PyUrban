from rat_with_exc import Runner as Runner
from rat_with_exc import Tournament as Tournament

import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):
    def setUp(self):
        logging.info("Начинаем тест бегуна")

    def test_init_correct(self):
        try:
            runner = Runner("Alice", 10)
            self.assertEqual(runner.name, "Alice")
            self.assertEqual(runner.speed, 10)
            self.assertEqual(runner.distance, 0)
            logging.info("Тест test_init_correct - успешно")
        except Exception as exc:
            logging.info("Тест test_init_correct - ошибка")
            logging.info(exc)

    def test_init_wrong_name(self):
        try:
            runner = Runner(123, 10)  # передаем не строку в name
            logging.warning("Класс Runner принял в качестве имени int!!!")
        except Exception as exc:
            logging.info(f"test_init_wrong_name - ошибка: {exc}")


    def test_init_wrong_speed(self):
        try:
            runner = Runner("Bob", -5)
            logging.warning("Класс Runner принял отрицательную скорость!!!")# передаем отрицательное значение speed
        except Exception as exc:
            logging.info(f"test_init_wrong_speed - ошибка: {exc}")


    def test_run(self):
        try:
            runner = Runner("Charlie", 5)
            runner.run()
            self.assertEqual(runner.distance, 10)  #  Проверяем, что distance увеличилась на 10
            logging.info("test_run - успешно")
        except Exception as exc:
            logging.warning(f"test_run - ошибка: {exc}")

    def test_walk(self):
        try:
            runner = Runner("David", 5)
            runner.walk()
            self.assertEqual(runner.distance, 5)  # Проверяем, что distance увеличилась на 5
            logging.info("test_walk - успешно")
        except Exception as exc:
            logging.warning(f"test_walk - ошибка: {exc}")
class TournamentTest(unittest.TestCase):
    def setUp(self):
        logging.info("Начинаем тест состязания")

    def test_start_empty(self):
        try:
            tournament = Tournament(100)
            finishers = tournament.start()
            self.assertEqual(finishers, {}) # Проверяем, что финишеры пустые
            logging.info("test_start_empty - успешно")
        except Exception as exc:
            logging.warning(f"test_start_empty не пройден: {exc}")


    def test_start_one_participant(self):
        try:
            runner1 = Runner("Alice", 10)
            tournament = Tournament(100, runner1)
            finishers = tournament.start()
            self.assertEqual(finishers, {1: runner1})  # Проверяем, что Alice - победитель
            logging.info("test_start_one_participant - успешно")
        except Exception as exc:
            logging.warning(f"test_start_empty не пройден: {exc}")


if __name__ == '__main__':
    unittest.main()
