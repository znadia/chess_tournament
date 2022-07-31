class Round:
    
    def __init__(self, name, all_players):

        self.name = name
        self.all_players = all_players
        self.all_players_keys = list(all_players.keys())
        self.filtered_players = []

    def __str__(self):
        return f"{self.name}, {self.all_players}, {self.filtered_players}"

    
    def display_match(self):

        length = len(self.all_players_keys)
        middle_list = length // 2
        
        first_half = self.all_players_keys[:middle_list]
        second_half = self.all_players_keys[middle_list:]
    
        for a,b in zip(first_half,second_half):
            self.filtered_players.append([a,b])

    
