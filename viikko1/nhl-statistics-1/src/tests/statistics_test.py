import unittest
from statistics import Statistics
from player  import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):

    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_luo_Statistics(self):
        self.assertEqual(len(self.statistics._players), 5)

    def test_search_player(self):
        player = self.statistics.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_not_found(self):
        player = self.statistics.search("Selänne")
        self.assertEqual(player, None)
    
    def test_team(self):
        team = self.statistics.team("EDM")
        self.assertEqual(len(team), 3)
        self.assertEqual(team[0].name, "Semenko")
        self.assertEqual(team[1].name, "Kurri")
        self.assertEqual(team[2].name, "Gretzky")
    
    def test_top_scorers(self):
        players = self.statistics.top_scorers(2)
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")


    