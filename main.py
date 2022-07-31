from Model.tournament import Tournament
from Model.player import Player
from Model.round import Round
from Model.match import Match
import random
import re
from rich.console import Console
from rich.table import Table

console = Console()

all_players = {}

################################# FCT Création tournoie #####################################

def display_info_tournament():

    t_name = input("Nom du tournoi: ")
    t_place = input("Lieu du tournoi: ")
    t_date = input("Date du tournoi: ")
    t_time_control = input("Controle du temps ")
    #t_players = input("Controle du temps ")
    t_description = input("Description du tournoi ")
    t = Tournament(t_name,t_place,t_date,t_time_control,t_players,t_description)


############################# FCT REGEX DATE DE NAISSANCE ###################################

def int_date_birthday():

    regex = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
    result = input("votre date de naissance jj/mm/aaaa: ")
    
    while not re.findall(regex, result) :
        result = input("Veuillez entrer une date de naissance valide: ")
    
    return result

################################# FCT CRÉATION JOUEURS ######################################

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
"""
print("\ndic all_player[j2]:      ", all_players['joueur_2'])        b, b, 11/11/1111, b    
print("\nclasse round all_player: ", first_round.all_players)            {'joueur_1': a, 'joueur_2': b}
print("\ndic all_player:      ", all_players)                            {'joueur_1': a, 'joueur_2': b}
first_round.display_match()
print("\nfonction filtre:     ", first_round.filtered_players)             [('joueur_1', 'joueur_2')]
print("\nclasse round all_player_key: ", first_round.all_players_keys)      ['joueur_1', 'joueur_2']
"""
################################# TABLEAU JOUEURS #####################################

def display_table_tournament(players, a, b):

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Joueurs")
    table.add_column("Prénom", style="dim", width=12)
    table.add_column("Classement")
    table.add_column("Score")

    for player in players:
        table.add_row(
            player, f"{players[player].first_name} {players[player].name}", a, b
        )

    console.print(table)

#print(first_round.all_players['joueur_2'].name)

display_table_tournament(first_round.all_players, "0", "0")

first_round.display_match()


################################# TABLEAU MATCHES #####################################

def display_table_first_round(players, a, b):

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Matches")
    table.add_column("Classement")
    table.add_column("Score")

    for player in players:
        table.add_row(
            f"{player[0]} vs {player[1]}", a, b
        )

    console.print(table)

display_table_first_round(first_round.filtered_players, "0", "0")

############################### FCT CRÉATION MATCHES ##################################

"""
first_match = first_round.filtered_players[0]
print(type(first_match))
print(first_match)


match_1 = Match(name="match_1",players_pair=first_match)




print(" ")
print("joueur: ", match_1.score_player1)
print(type(match_1.score_player1))


for i in range(9):
    match_1.score_player1 += 1
print(match_1.score_player1)
print(match_1)
match_1.score_player1 += 0.5
print(match_1)


"""
def score_match(first_match, nom):


    #first_match = first_round.filtered_players[i]
    list_score = [1.0, 0.5, 0.0]
    nom = Match(name=nom,players_pair=first_match)
    tuple_match = ([nom.player1, nom.score_player1], [nom.player2, nom.score_player2])
    
    for x in tuple_match:

        response = input("Veuillez entrer le score du " + x[0] + ": ")
        print("v avant =", x[1])
        while response not in list_score:
            response = input("Le score n'est pas bon: ")
            response =float(response)

        x[1] += response
        print("v avant =", x[1])
        print("lol", nom)



#score_match(first_round.filtered_players[0], "match_1")
#print(nom)
