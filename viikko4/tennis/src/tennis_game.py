class TennisGame:

    class Player:
        def __init__(self, name):
            self.name = name
            self.score = 0

        def get_point_name(self):

            if self.score == 0:
                return "Love"
            elif self.score == 1:
                return "Fifteen"
            elif self.score == 2:
                return "Thirty"
            elif self.score == 3:
                return "Forty"

    def __init__(self, player1_name, player2_name):
        self.player1 = TennisGame.Player(player1_name)
        self.player2 = TennisGame.Player(player2_name)
        

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.score += 1
        else:
            self.player2.score += 1

  

    def get_score(self):
        score = ""

        if self.player1.score == self.player2.score:

            if self.player1.score < 4:
                score = self.player1.get_point_name() + "-All"
            else:
                score = "Deuce"


        elif self.player1.score < 4 and self.player2.score < 4:
            score = self.player1.get_point_name() + "-" + self.player2.get_point_name()

        else:

            if abs(self.player1.score - self.player2.score) <= 1:
                score = "Advantage "
            else:
                score = "Win for "

            
            if self.player1.score > self.player2.score:
                score += self.player1.name
            else:
                score += self.player2.name            



        return score
