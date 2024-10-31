import runner_and_tournament
import unittest

is_frozen = True
class RunnerTest(unittest.TestCase):
    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_walk(self):
        turtle = runner_and_tournament.Runner("Донателло")
        for _ in range(10):
            turtle.walk()
        self.assertEqual(turtle.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        turtle = runner_and_tournament.Runner("Микеланджело")
        for _ in range(10):
            turtle.run()
        self.assertEqual(turtle.distance, 100)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_challenge(self):
        turtle1 = runner_and_tournament.Runner("Леонардо")
        turtle2 = runner_and_tournament.Runner("Рафаэль")
        for _ in range(10):
            turtle1.run()
            turtle2.walk()
        self.assertNotEqual(turtle1.distance, turtle2.distance)


if __name__ == '__main__':
    unittest.main()
