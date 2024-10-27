import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.speed1 = 10
        self.speed2 = 9
        self.speed3 = 3
        self.Usain = runner_and_tournament.Runner("Usain", self.speed1)
        self.Andrey = runner_and_tournament.Runner("Andrey", self.speed2)
        self.Nick = runner_and_tournament.Runner("Nick", self.speed3)



    @classmethod
    def tearDownClass(cls):
        for element in cls.all_results:
            print(element)


    def test_tournament_Usain_Nick(self):
        tournament = runner_and_tournament.Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.assertTrue(results[1] == "Usain")
        self.assertTrue(results[2] == "Nick")
        self.all_results.append(results)

    def test_tournament_Andrey_Nick(self):
        tournament = runner_and_tournament.Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.assertTrue(results[1] == "Andrey")
        self.assertTrue(results[2] == "Nick")
        self.all_results.append(results)

    def test_tournament_Usain_Andrey_Nick(self):
        tournament = runner_and_tournament.Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.assertTrue(results[1] == "Usain")
        self.assertTrue(results[2] == "Andrey")
        self.assertTrue(results[3] == "Nick")
        self.all_results.append(results)

if __name__ == '__main__':

    #  Запустим тесты с помощью unittest.main()
    unittest.main()
