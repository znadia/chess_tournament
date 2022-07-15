from Model.player import Player
from Model.round import Round
import random
from rich.console import Console
from rich.table import Table

#list_players = ["1", "2", "3", "4", "5", "6", "7", "8"]
list_players = []

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

print(all_players['joueur_2'].d_o_b)

first_round = Round(name="premier_round",players=all_players)
print(first_round.players)


#creer une instance de tournoi (joueur en liste (players))instance.methode

#
"""
console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Match", style="dim", width=12)
table.add_column("Classement")

table.add_row(
    "Dev 20, 2019", "Star Wars: The Rise of Skywalker",
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
)
console.print(table)
"""