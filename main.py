from Model.player import Player
from Model.round import Round
import random
import re
from rich.console import Console
from rich.table import Table

all_players = {}

#def display_players_tournament():

def int_date_birthday():

    regex = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
    result = ""

    result = input("votre date de naissance jj/mm/aaaa: ")
    
    while not re.findall(regex, result) :
        result = input("Veuillez entrer une date de naissance valide: ")
    
    return result


def create_players():

    for i in range(1, 3):
        p_name = input("ton nom? ")
        p_first_name = input("ton prénom? ")
        p_d_o_b = int_date_birthday() 
        p_sex = input("Homme ou Femme? ")
        p = Player(p_name,p_first_name,p_d_o_b,p_sex)
        all_players['joueur_' + str(i)] = p

create_players()

first_round = Round(name="premier_round",all_players=all_players)

print(all_players['joueur_2'])
print(first_round.all_players)
first_round.display_match()
print(first_round.filtered_players)
#creer une instance de tournoi (joueur en liste (players))instance.methode
print(first_round.all_players_keys)


console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Joueurs", style="dim", width=12)
table.add_column("Classement")

for player in first_round.all_players_keys:
    table.add_row(
        player, "0",
    )

console.print(table)
