import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_search(self):
        answer = self.stats.search("Kurri")
        self.assertEqual(str(answer), "Kurri EDM 37 + 53 = 90")
        answer = self.stats.search("Litmanen")
        self.assertEqual(answer, None)

    def test_team(self):
        answer = self.stats.team("EDM")
        edm_team = ["Semenko", "Kurri", "Gretzky"]
        i = 0
        for player in answer:
            self.assertEqual(player.name, edm_team[i])
            i += 1

    def test_top(self):
        answer = self.stats.top(1)
        self.assertEqual(len(answer), 1)
        self.assertEqual(answer[0].name, "Gretzky")




# f"{answer.name} {answer.team} {answer.goals} + {answer.assists} = {answer.points}"