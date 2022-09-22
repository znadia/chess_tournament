from model.tournament import Tournament
from model.player import Player
from model.round import Round
from model.match import Match
import database
import json
import random
import re
import inquirer
import datetime
from rich.console import Console
from rich.table import Table



console = Console()

dic_info_tournament = {}

dic_all_players = {}

################################################
questions = [
    inquirer.List(
        "size",
        message="Que voulez-vous faire ?",
        choices=["Créer un tournoi","Visualiser les rapports", "Quitter"],
    ),
]
answers = inquirer.prompt(questions)

print(answers["size"])

if answers["size"] == "Quitter":
    print("Au revoir")
    quit()

################################# FCT Création tournoie #####################################


def create_info_tournament():

    t_name = input("Nom du tournoi: ")
    t_place = input("Lieu du tournoi: ")
    t_date = input("Date du tournoi: ")
    t_time_control = input("Controle du temps ")
    t_players = create_players()
    t_description = input("Description du tournoi ")
    t = Tournament(t_name, t_place, t_date, t_time_control, t_description)
    dic_info_tournament[t_name] = t


    return dic_info_tournament


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
        p = Player(p_name, p_first_name, p_d_o_b, p_sex)
        dic_all_players["joueur_" + str(i)] = p
    

    return dic_all_players

#print("fonction dic: ", dic_all_players['joueur_1'].__dict__)

################################# CRÉATION Nom DataBase ######################################


create_info_tournament()

name_tournament = list(dic_info_tournament.keys())[0]

db_file = database.create_db_file(name_tournament)


################################################

def what_to_do(fct_db):

    questions = [
        
        inquirer.List(
            "size",
            message="Que voulez-vous faire ?",
            choices=["Sauvegarder les informations", "Continuer", "Quitter"],
        ),
    ]
    answers = inquirer.prompt(questions)

    if answers["size"] == "Sauvegarder les informations":
        fct_db == True

    if answers["size"] == "Quitter":
        print("Au revoir")
        quit()


what_to_do(database.insert_db_info(dic_info_tournament, db_file))
#database.insert_db_info(dic_all_players, db_file)


#database.display_db(db_file)

"""

first_round = Round(name="premier_round", all_players=dic_all_players)


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

first_round.display_match()

dic_filtered = {}



def dic_round_match(dic_filtered, name_round, list_filtered_player):
    dic_filtered[name_round] = list_filtered_player
    return dic_filtered

fonction = dic_round_match(dic_filtered, first_round.name, first_round.filtered_players)

print("fonction dic player ---->    ", fonction)
print(type(fonction))


database.insert_db_round(fonction, db_file)


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


def add_score_match(nom, dic_player):

    list_score = [0.0, 0.5, 1.0]
    score_p1 = ""
    score_p2 = ""

    while score_p1 not in list_score:
        score_p1 = input("Veuillez entrer le score du " + nom.player1 + ": ")
        score_p1 = float(score_p1)

    nom.score_player1 += score_p1
    dic_player[nom.player1].score += score_p1

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
list_match = first_round.filtered_players
list_players = first_round.all_players_keys

for i in range(len(list_match)):
    matches = list_match[i]
    i += 1
    print(i)
    name_match = "match_" + str(i)
    print(name_match)
    a = display_instance_match(name_match, matches)
    add_score_match(a, dic_all_players)

display_table_first_round(list_match, "0", "0")

display_table_tournament(first_round.all_players, "0")

####################### création des autres matches ##################################


# liste des matches passés

def check_match(list_match, player_1, player_2):
    sorted_player = tuple(sorted([player_1, player_2]))
    if sorted_player in list_match:
        return False
    else:
        return sorted_player


def new_round(list_players, list_match):

    list_players_cop = list_players.copy()
    new_match = []
    i = 0
    x = 1
    while i < len(list_players_cop):
        while x < len(list_players_cop):
            if list_players_cop[i] != list_players_cop[x]:
                ret = check_match(list_match, list_players_cop[i], list_players_cop[x])
                if ret != False:
                    new_match.append(ret)
                    del list_players_cop[x]
                    del list_players_cop[i]
                    x = 0
                    i = 0
            x += 1
    list_match.extend(new_match)
    return new_match


print(list_players)
print("filtered_player: ", list_match)

fonction = new_round(list_players, list_match)
print(fonction) 


print("joueur == 22 : ", list_players)
print("filtered_player 222 : ", list_match)

fonction2 = new_round(list_players, list_match)
print(fonction2) 
"""