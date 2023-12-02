class TennisGame:

    score_is_love = 0
    score_is_fifteen = 1
    score_is_thirty = 2
    score_is_fourty = 3
    score_is_more_than_fourty = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = TennisGame.score_is_love
        self.player2_score = TennisGame.score_is_love

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self.get_score_when_the_same_amount_of_points()
        elif self.player1_score >= TennisGame.score_is_more_than_fourty or self.player2_score >= TennisGame.score_is_more_than_fourty:
            score = self.get_score_when_other_has_advantage_or_has_won()
        else:
            score = self.get_score_when_other_is_leading_but_has_under_fourty_score()

        return score

    def get_score_when_the_same_amount_of_points(self):
        if self.player1_score == TennisGame.score_is_love:
            return "Love-All"
        elif self.player1_score == TennisGame.score_is_fifteen:
            return "Fifteen-All"
        elif self.player1_score == TennisGame.score_is_thirty:
            return "Thirty-All"
        else:
            return "Deuce"

    def get_score_when_other_has_advantage_or_has_won(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_score_when_other_is_leading_but_has_under_fourty_score(self):
        temp_score = 0
        score = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score

            if temp_score == TennisGame.score_is_love:
                score = score + "Love"
            elif temp_score == TennisGame.score_is_fifteen:
                score = score + "Fifteen"
            elif temp_score == TennisGame.score_is_thirty:
                score = score + "Thirty"
            elif temp_score == TennisGame.score_is_fourty:
                score = score + "Forty"

        return score
