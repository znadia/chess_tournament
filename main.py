from Model.player import Player
from Model.round import Round
import random
from rich.console import Console
from rich.table import Table

all_players = {}

#def display_players_tournament():


def create_players():

    for i in range(1, 3):
        p_name = input("ton nom? ")
        p_first_name = input("ton prénom? ")
        # 3 input
        p_d_o_b = int(input("Date de naissance? ")) 
        p_sex = input("Homme ou Femme? ")
        p = Player(p_name,p_first_name,p_d_o_b,p_sex)
        all_players['joueur_' + str(i)] = p

create_players()

print(all_players['joueur_2'])

first_round = Round(name="premier_round",all_players=all_players)
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
