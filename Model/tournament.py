

class Tournament:
    
    def __init__(self, name, place, date, nbr_rounds=4, time_control, players, description):
        
        self.name = name
        self.place = place
        self.date = date
        self.nbr_rounds = nbr_rounds
        self.time_control = time_control
        self.players = players
        self.description = description
