class GameLogic:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1

    def add_points(self, points):
        if self.current_player == 1:
            self.player1_score += points
        else:
            self.player2_score += points

    def switch_turn(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def get_scores(self):
        return self.player1_score, self.player2_score

    def get_current_player(self):
        return self.current_player