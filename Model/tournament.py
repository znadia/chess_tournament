

class Tournament:
    
    def __init__(self, name, place, date, nbr_rounds, time_control, players, pairs_matched, description, rounds):
        
        self.name = name
        self.place = place
        self.date = date
        self.nbr_rounds = nbr_rounds
        self.time_control = time_control
        self.players = players
        self.pairs_matched = pairs_matched
        self.description = description
        self.rounds = rounds

    def __str__(self):
        return f"{self.name}{self.place}{self.date}{self.nbr_rounds}{self.time_control}{self.players}"
    
    def __repr__(self):
        return f"{self.name}{self.place}{self.date}{self.nbr_rounds}{self.time_control}{self.players}"

