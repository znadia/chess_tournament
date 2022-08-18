from model.tournament import Tournament
from model.player import Player
from model.round import Round
from model.match import Match
import database
import json
import random
import re
import inquirer
from rich.console import Console
from rich.table import Table



console = Console()

all_players = {}


questions = [
    inquirer.List(
        "size",
        message="Que voulez-vous faire ?",
        choices=["Créer un tournoi", "Quitter"],
    ),
]
answers = inquirer.prompt(questions)

# print(answers["size"])

if answers["size"] == "Quitter":
    print("Au revoir")
    quit()

################################# FCT Création tournoie #####################################


def display_info_tournament():

    t_name = input("Nom du tournoi: ")
    t_place = input("Lieu du tournoi: ")
    t_date = input("Date du tournoi: ")
    t_time_control = input("Controle du temps ")
    # t_players = input("Controle du temps ")
    t_description = input("Description du tournoi ")
    t = Tournament(t_name, t_place, t_date, t_time_control, t_players, t_description)


############################# FCT REGEX DATE DE NAISSANCE ###################################


def int_date_birthday():

    regex = re.compile(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$")
    result = input("votre date de naissance jj/mm/aaaa: ")

    while not re.findall(regex, result):
        result = input("Veuillez entrer une date de naissance valide: ")

    return result


################################# FCT CRÉATION JOUEURS ######################################


def create_players():

    for i in range(1, 5):
        p_name = input("ton nom: ")
        p_first_name = input("ton prénom: ")
        # p_d_o_b = int_date_birthday()
        p_d_o_b = input("date de naissance: ")
        p_sex = input("Homme ou Femme: ")
        p_score = 0
        p = Player(p_name, p_first_name, p_d_o_b, p_sex)
        all_players["joueur_" + str(i)] = p


create_players()

b = "ddd"

for a, b in all_players.items():
    print("l'élément de clé", a, "vaut", b)
    print(type(b))
    print("\n")

print(all_players)

"""
#print(b)
print(type(all_players))

database.insert(all_players.copy())

#parsed_json = json.dump(all_players)
#print(parsed_json)

first_round = Round(name="premier_round", all_players=all_players)



################################# TABLEAU JOUEURS #####################################


def display_table_tournament(players, a):

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Joueurs")
    table.add_column("Prénom", style="dim", width=12)
    table.add_column("Classement")
    table.add_column("Score")

    for player in players:
        table.add_row(
            player,
            f"{players[player].first_name} {players[player].name}",
            a,
            f"{players[player].score}",
        )

    console.print(table)


display_table_tournament(first_round.all_players, "0")
print(first_round.all_players)
print(all_players["joueur_1"].score)
first_round.display_match()


################################# TABLEAU MATCHES #####################################


def display_table_first_round(players, a, b):

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Matches")
    table.add_column("Classement")
    table.add_column("Score")

    for player in players:
        table.add_row(f"{player[0]} vs {player[1]}", a, b)

    console.print(table)


display_table_first_round(first_round.filtered_players, "0", "0")

############################### FCT CRÉATION MATCHES ##################################


def display_instance_match(name_match, players_match):

    name_match = Match(name=name_match, players_pair=players_match)
    return name_match


############################### FCT SCORE ##################################


def score_match(nom, dic_player):

    list_score = [0.0, 0.5, 1.0]
    score_p1 = ""
    score_p2 = ""

    while score_p1 not in list_score:
        score_p1 = input("Veuillez entrer le score du " + nom.player1 + ": ")
        score_p1 = float(score_p1)

    nom.score_player1 += score_p1
    dic_player[nom.player1].score += score_p1
    print("PRINTTTTT", dic_player[nom.player1].score)

    if score_p1 == 0.0:
        list_score = [1.0]

    if score_p1 == 0.5:
        list_score = [0.5]

    if score_p1 == 1.0:
        list_score = [0.0]

    while score_p2 not in list_score:
        score_p2 = input("Veuillez entrer le score du " + nom.player2 + ": ")
        score_p2 = float(score_p2)

    nom.score_player2 += score_p2
    dic_player[nom.player2].score += score_p2


print(first_round.filtered_players)

############################### FCT CRÉATION INSTANCES MATCHES ##################################

for i in range(len(first_round.filtered_players)):
    matches = first_round.filtered_players[i]
    i += 1
    print(i)
    name_match = "match_" + str(i)
    print(name_match)
    a = display_instance_match(name_match, matches)
    score_match(a, all_players)

display_table_first_round(first_round.filtered_players, "0", "0")

display_table_tournament(first_round.all_players, "0")
"""