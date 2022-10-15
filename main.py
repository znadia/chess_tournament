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
from view.view import ViewClass


viewclass = ViewClass()


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

    for i in range(1, 9):
        p_name = input("ton nom: ")
        p_first_name = input("ton prénom: ")
        # p_d_o_b = int_date_birthday()
        p_d_o_b = input("date de naissance: ")
        p_sex = input("Homme ou Femme: ")
        p = Player(p_name, p_first_name, p_d_o_b, p_sex)
        dic_all_players["joueur_" + str(i)] = p
    

    return dic_all_players


################################# CRÉATION Nom DataBase ######################################


create_info_tournament()

name_tournament = list(dic_info_tournament.keys())[0]

db_file = database.create_db_file(name_tournament)



################################################

def what_to_do(dic):

    questions = [
        
        inquirer.List(
            "size",
            message="Que voulez-vous faire ?",
            choices=["Sauvegarder les informations", "Continuer", "Quitter"],
        ),
    ]
    answers = inquirer.prompt(questions)

    if answers["size"] == "Sauvegarder les informations":
        database.insert_db_info(dic, db_file)

    if answers["size"] == "Quitter":
        print("Au revoir")
        quit()


what_to_do(dic_info_tournament)
database.insert_db_info(dic_all_players, db_file)




#############first_round = Round(name="premier_round", all_players=dic_all_players)



################################# TABLEAU JOUEURS ########
viewclass.display_table_tournament(dic_all_players)


###########first_round.display_match()



"""
###################### insert dans la db les premier match de filtered player ####################

dic_filtered = {}

def dic_round_match(dic_filtered, name_round, list_filtered_player):
    dic_filtered[name_round] = list_filtered_player
    return dic_filtered

fonction = dic_round_match(dic_filtered, first_round.name, first_round.filtered_players)


#database.insert_db_round(fonction, db_file)
"""

############################### FCT CRÉATION Round ##################################

def get_matches(list_match):
    for i in range(len(list_match)):
            players_match = list_match[i]
            i += 1
            name_match = "match_" + str(i)
            match_to_play = Match(name=name_match, players_pair=players_match)
            match_to_play.add_score_match(dic_all_players)
            print(match_to_play.__repr__())

##################  Fonction pour trier et classer ###################

# Récupère la score du nom sous forme de liste
def get_score_sorted(name_round):
    list_score = []
    for k, v in name_round.all_players.items():
        value = name_round.all_players[k].score
        list_score.append(value)
    sort_list = sorted(list_score, reverse = True)
    return sort_list

"""
# Trie les valeur 
score_sorted = sorted(list_score, reverse = True)
print("trier : ", score_sorted)
"""



# pour retrouver la clef d'une valeur (valeur)

#######
def find_key(v, dic_players):
    for k, val in dic_players.items(): 
        if v == val.score:
            return k

# Crée une liste trier des clefs
def ranking_sorted(name_round, score_sorted):
    players_cop = name_round.all_players.copy()
    player_ranked = []
    i = 1
    for score in score_sorted:
        k = find_key(score, players_cop)
        name_round.all_players[k].ranking = i
        player_ranked.append(k)
        del(players_cop[k])
        i += 1
    return player_ranked



####################### création des autres matches ##################################

# liste des matches passés

###############
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


#############################################################################################################################################



nbr_rounds = dic_info_tournament[name_tournament].nbr_rounds
list_round = dic_info_tournament[name_tournament].round_played
past_matches = dic_info_tournament[name_tournament].dic_rounds

for nbr in range(nbr_rounds):
    i = nbr + 1
    name_round = "round_" + str(i)
    name_round = Round(name=name_round, all_players=dic_all_players)
    if i == 1:
        name_round.display_match()
        list_match = name_round.filtered_players
        viewclass.display_table_round(list_match)
        past_matches[name_round] = list_match
        list_round.append(list_match)
        get_matches(list_match)
        score_sorted = get_score_sorted(name_round)
        players_ranks = ranking_sorted(name_round, score_sorted)
        new_match = new_round(players_ranks, list_round)
        viewclass.display_table_round(new_match)
        viewclass.display_table_tournament(dic_all_players)
        



"""
    #list_round.append(name_round)
    

viewclass.display_table_round(list_match)

viewclass.display_table_tournament(dic_all_players)

####################### création des autres matches ##################################

# liste des matches passés

###############
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





viewclass.display_table_tournament(dic_all_players)

print("joueur classé  -->   ", player_ranked)

fonction = new_round(player_ranked, list_match)
print(fonction)

"""