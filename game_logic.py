class GameLogic:
    """
    Manages the core state of the Jeopardy game, including tracking
    player scores and determining whose turn it is.
    """
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1

    def add_points(self, points):
        # Adds the specified point value to the current active player's total score.
        if self.current_player == 1:
            self.player1_score += points
        else:
            self.player2_score += points

    def switch_turn(self):
        # Toggles the active turn back and forth between Player 1 and Player 2.
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def get_scores(self):
        # Returns a tuple containing the current running scores for both players.
        return self.player1_score, self.player2_score

    def get_current_player(self):
        # Returns an integer (1 or 2) representing which player's turn it currently is.
        return self.current_player
