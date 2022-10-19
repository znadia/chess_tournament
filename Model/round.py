from datetime import datetime

class Round:
    
    def __init__(self, name, all_players, start_time=None, end_time=None):

        self.name = name
        self.all_players = all_players
        self.all_players_keys = list(all_players.keys())
        self.filtered_players = []
        self.match_played = []
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name}, {self.match_played}, {self.start_time}, {self.start_time}"
    
    def __repr__(self):
        return f"{self.name}, {self.match_played}, {self.start_time}, {self.start_time}"

    def display_match(self):

        length = len(self.all_players_keys)
        middle_list = length // 2
        
        first_half = self.all_players_keys[:middle_list]
        second_half = self.all_players_keys[middle_list:]
    
        for a,b in zip(first_half,second_half):
            self.filtered_players.append([a,b])

    def get_times(self):
        # Récupère l'heure
        return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")[:-3]

    
 
    