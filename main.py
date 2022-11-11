from model.tournament import Tournament
from model.player import Player
from model.round import Round
import controller.utils
import controller.info
from view.table import ViewTable
from view.menu import ViewMenu


viewtable = ViewTable()
viewmenu = ViewMenu()
info = controller.info
utils = controller.utils


dic_info = {}
dic_players = {}


viewmenu.display_start_menu()


def create_players():
    for i in range(1, 9):
        p_name = input("Nom: ")
        p_first_name = input("Prénom: ")
        #p_d_o_b = info.int_date_birthday()
        p_d_o_b = input("d_o_b: ")
        p_sex = input("Sexe: ")
        #p_sex = info.check_sex()
        p = Player(p_name, p_first_name, p_d_o_b, p_sex, 0, 0)
        dic_players["joueur_" + str(i)] = p
    return dic_players


def create_info_tournament():
    name = input("Nom du tournoi: ")
    place = input("Lieu du tournoi: ")
    date = input("Date du tournoi: ")
    #t_c = info.check_time_control()
    t_c = input("time controle: ")
    players = info.check_players(create_players())
    print("kkk  ", dic_players)
    nbr_rounds = info.check_nbr_round()
    desc = input("Description du tournoi ")
    t = Tournament(name, place, date, nbr_rounds, t_c, players, [], desc, [])
    dic_info[name] = t

    return dic_info


create_info_tournament()

name_file = list(dic_info.keys())[0]
db_file = viewmenu.create_name_file(name_file)
print("55   ", dic_info[name_file].players)

def deserialize_players(dic_file, dic_players, name_file):
    dic_players.clear()
    for players in dic_file[name_file].get('players'):
        for key, value in players.items():
            p = []
            for v in value.values():
                p.append(v)
        pl = Player(p[0], p[1], p[2], p[3], p[4], p[5])
        dic_players[key] = pl

    return dic_players



"""
def deserialize_round(dic_file, name_file):
    list_round = []

    for i in dic_file[name_file].get('rounds'):
        list_round.append(i)
    return list_round  
"""

def deserialize_tournement(dic_info, name_file, obj_pl):

    x = []
    lst_r = dic_info[name_file].get('rounds')
    lst_m = dic_info[name_file].get('pairs_matched')
    for v in dic_info[name_file].values():
        x.append(v)
    t = Tournament(x[0], x[1], x[2], x[3], x[4], obj_pl, lst_m, x[7], lst_r)
    dic_info[name_file] = t

    return dic_info



viewmenu.display_menu(dic_info, db_file)

viewtable.display_table_tournament(dic_players)

#nbr_rounds = int(dic_info[name_file].nbr_rounds)
#rounds = dic_info[name_file].rounds
pairs_matched = dic_info[name_file].pairs_matched
#players = dic_info[name_file].players


for nbr in range(int(dic_info[name_file].nbr_rounds)):
    i = nbr + 1
    name_round = "round_" + str(i)
    name_round = Round(name=name_round, all_players=dic_players)
    if i == 1:
        # Déroulement d'un Round/Matches
        viewtable.display_start_time(name_round)####
        name_round.first_round()
        pairs_matched.extend(name_round.first_round()) # Pairs_match = [['joueur_1', 'joueur_5'], ['joueur_2', 'joueur_6'], ['joueur_3', 'joueur_7'], ['joueur_4', 'joueur_8']]
        viewtable.display_table_round(pairs_matched, name_round)
        utils.get_matches(pairs_matched, dic_players, name_round.matches) #Crée le match et le score 
        viewtable.display_end_time(name_round)#####
        dic_info[name_file].rounds.append(name_round.return_dic_round())#Enregistre le round dans dic_info




        dic_info[name_file].players = info.check_players(dic_players)
        print("119    ", dic_info[name_file].players)
        #players_ranks = utils.create_ranking(name_round)  ####   ['joueur_3', 'joueur_5', 'joueur_8', 'joueur_2', 'joueur_6', 'joueur_1', 'joueur_4', 'joueur_7']
        #dic_rank = utils.sorted_players(dic_players, players_ranks)
        dic_rank = {}
        viewtable.display_table_tournament(dic_players)
        print("player 1 131 ===  ", dic_info[name_file].players)
        #viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, name_file)
        ###############################################################
        
        
        dic_info = viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, "lola")
        name_file = 'lola'
        db_file = viewmenu.create_name_file(name_file)
        print("143  ===  ", dic_info[name_file])
        
        p = deserialize_players(dic_info, dic_players, name_file)
        deserialize_tournement(dic_info, name_file, p)
        print("######################### \n", dic_info[name_file])
        print("player 1 ===  ", dic_players)
    
    if i >= 2:
        players_ranks = utils.create_ranking(name_round)  ####   ['joueur_3', 'joueur_5', 'joueur_8', 'joueur_2', 'joueur_6', 'joueur_1', 'joueur_4', 'joueur_7']
        print("playe rank 142 =====   ", players_ranks)
        #dic_rank = utils.sorted_players(dic_players, players_ranks)
        dic_rank = {} ############
        viewtable.display_start_time(name_round) ####
        pairs_matched = dic_info[name_file].pairs_matched
        list_new_match = utils.new_round(players_ranks, pairs_matched) #Créer le nouveau match
        print("pairs_match dic 138    = ",  dic_info[name_file].pairs_matched)
        viewtable.display_table_round(list_new_match, name_round)
        
        utils.get_matches(list_new_match, dic_players, name_round.matches)
        viewtable.display_end_time(name_round)#####
        dic_info[name_file].rounds.append(name_round.return_dic_round())
        print("156 ===== ", dic_info[name_file])
    


        #players_ranks = utils.create_ranking(name_round)

        #dic_rank = utils.sorted_players(dic_players, players_ranks)
        viewtable.display_table_tournament(dic_rank)


        dic_info[name_file].players = info.check_players(dic_players)

        #  
        print("nbr de round  ", int(dic_info[name_file].nbr_rounds))
        print("lloooppppp 2222 ", dic_info[name_file].name)
        print("tttttt 222222  ", dic_info[name_file].players)
        viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, name_file)
        ##################################################################
        print("name_file == ", name_file)

    #viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, name_file)
       
  


print("\n")
print("Le gagnant est  :  ", players_ranks[0])
