from model.tournament import Tournament
from model.player import Player
from model.round import Round
import controller.utils
import controller.info 
import database
import json
import random
import inquirer
from view.view import ViewClass


info = controller.info
utils = controller.utils
viewclass = ViewClass()
dic_info_tournament = {}
dic_all_players = {}



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

    name = input("Nom du tournoi: ")
    place = input("Lieu du tournoi: ")
    date = input("Date du tournoi: ")
    time_control = info.check_time_control()
    players = create_players()
    nbr_rounds = info.check_nbr_round()
    description = input("Description du tournoi ")
    t = Tournament(name, place, date, time_control, nbr_rounds, description)
    dic_info_tournament[name] = t


    return dic_info_tournament



################################# FCT CRÉATION JOUEURS ######################################


def create_players():

    for i in range(1, 9):
        p_name = input("Nom: ")
        p_first_name = input("Prénom: ")
        # p_d_o_b = info.int_date_birthday()
        p_d_o_b = input("Date de naissance: ")
        #p_sex = info.check_sex()
        p_sex = input("Homme ou Femme: ")
        p = Player(p_name, p_first_name, p_d_o_b, p_sex)
        dic_all_players["joueur_" + str(i)] = p
    

    return dic_all_players


################################# CRÉATION Nom DataBase ######################################

create_info_tournament()

name_tournament = list(dic_info_tournament.keys())[0]

db_file = database.create_db_file(name_tournament)


################################################

def display_menu(dic):

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


display_menu(dic_info_tournament)
database.insert_db_info(dic_all_players, db_file)


viewclass.display_table_tournament(dic_all_players)


"""
###################### insert dans la db les premier match de filtered player ####################

dic_filtered = {}

def dic_round_match(dic_filtered, name_round, list_filtered_player):
    dic_filtered[name_round] = list_filtered_player
    return dic_filtered

fonction = dic_round_match(dic_filtered, first_round.name, first_round.filtered_players)


#database.insert_db_round(fonction, db_file)
"""

#############################################################################################################################################

nbr_rounds = dic_info_tournament[name_tournament].nbr_rounds
list_match_played = dic_info_tournament[name_tournament].round_played
dic_rounds = dic_info_tournament[name_tournament].dic_rounds

for nbr in range(nbr_rounds):
    i = nbr + 1
    name_round = "round_" + str(i)
    name_round = Round(name=name_round, all_players=dic_all_players)
    if i == 1:
        name_round.display_match()
        list_new_match = name_round.filtered_players
        viewclass.display_table_round(list_new_match, name_round.name)
        #print("ii ===  ", i)
        dic_rounds[name_round] = list_new_match
        list_match_played.append(list_new_match) 
        utils.get_matches(list_new_match, dic_all_players)
        score_sorted = utils.get_score_sorted(name_round)
        players_ranks = utils.create_ranking(name_round, score_sorted)
        print("player_ranks    ::   ", players_ranks)
        viewclass.display_table_tournament(dic_all_players)
    if i >= 2:
        #print("\n")
        #print("La liste des rounds    >>   ", list_match_played)
        #print("\n")
        #print("Le dictionnaire des rounds    >>   ", dic_rounds)
        list_new_match = utils.new_round(players_ranks, list_match_played)
        viewclass.display_table_round(list_new_match, name_round.name)
        #print("iiiiiii ===  ", i)
        dic_rounds[name_round] = list_new_match
        list_match_played.append(list_new_match)
        utils.get_matches(list_new_match, dic_all_players)
        score_sorted = utils.get_score_sorted(name_round)
        players_ranks = utils.create_ranking(name_round, score_sorted)
        viewclass.display_table_tournament(dic_all_players)


print("\n")
print("Le gagnant est  :  ", players_ranks[0])
print("\n")
print("#################### FIN ############### ")
print("\n")
print("La liste des rounds    >>   ", list_match_played)
print("\n")
print("Le dictionnaire des rounds    >>   ", dic_rounds)
print("\n")


