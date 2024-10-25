import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        turtle = runner.Runner("Донателло")
        for _ in range(10):
            turtle.walk()
        self.assertEqual(turtle.distance, 50)

    def test_run(self):
        turtle = runner.Runner("Микеланджело")
        for _ in range(10):
            turtle.run()
        self.assertEqual(turtle.distance, 100)

    def test_challenge(self):
        turtle1 = runner.Runner("Леонардо")
        turtle2 = runner.Runner("Рафаэль")
        for _ in range(10):
            turtle1.run()
            turtle2.walk()
        self.assertNotEqual(turtle1.distance, turtle2.distance)


if __name__ == '__main__':
    unittest.main()
