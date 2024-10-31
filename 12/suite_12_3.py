import unittest
import tests_12_1
import tests_12_2

TestSuite = unittest.TestSuite()

TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)
