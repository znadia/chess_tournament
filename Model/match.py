class Match:
    def __init__(self, name, players_pair):
        self.name = name
        self.player1 = players_pair[0]
        self.score_player1 = 0
        self.player2 = players_pair[1]
        self.score_player2 = 0

    def __str__(self):
        return f"{self.name}, player1: {self.player1}, score_p1:"
        f" {self.score_player1}, player2: {self.player2}, score_p2: {self.score_player2}"

    def __repr__(self):
        return f"{self.name}, player1: {self.player1}, score_p1:"
        f" {self.score_player1}, player2: {self.player2}, score_p2: {self.score_player2}"
