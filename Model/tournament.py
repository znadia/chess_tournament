

class Tournament:
    
    def __init__(self, name, place, date, time_control, description, players=None, nbr_rounds=4):
        
        self.name = name
        self.place = place
        self.date = date
        self.nbr_rounds = nbr_rounds
        self.time_control = time_control
        self.players = players
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.place}, {self.date}, {self.nbr_rounds}, {self.time_control}, {self.players}, {self.description}"
    
    def __repr__(self):
        return f"{self.name}, {self.place}, {self.date}, {self.nbr_rounds}, {self.time_control}, {self.players}, {self.description}"