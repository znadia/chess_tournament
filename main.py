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
    for players in (dic_file[name_file].get('players')):
        for key, value in players.items():
            p = []
            for v in value.values():
                p.append(v)
        pl = Player(p[0], p[1], p[2], p[3], p[4], p[5])
        dic_players[key] = pl
    return dic_players


def deserialize_round(dic_file, name_file):
    list_round = []

    for i in dic_file[name_file].get('rounds'):
        list_round.append(i)
    return list_round  ############################# [0]



def deserialize_tournement(dic_info, name_file, obj_pl, obj_mt, obj_rd):

    x = []
    for v in dic_info[name_file].values():
        x.append(v)
    t = Tournament(x[0], x[1], x[2], x[3], x[4], obj_pl, obj_mt, x[7], obj_rd)
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
        viewtable.display_start_time(name_round)
        name_round.first_round()
        pairs_matched = name_round.first_round()
        viewtable.display_table_round(pairs_matched, name_round)
        matches = name_round.matches
        utils.get_matches(pairs_matched, dic_players, matches)
        score_sorted = utils.get_score_sorted(name_round)
        players_ranks = utils.create_ranking(name_round, score_sorted)
        dic_info[name_file].rounds.append(name_round.return_dic_round())
        viewtable.display_end_time(name_round)
        dic_info[name_file].players = info.check_players(dic_players)
        dic_rank = info.sorted_players(dic_players, players_ranks)
        viewtable.display_table_tournament(dic_rank)
        #viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, name_file)
        print("dic info 11 >>>  ", dic_info[name_file].players)
        print("nbr de round  ", int(dic_info[name_file].nbr_rounds))
        dic_info = viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, "lola")
        name_file = 'lola'
        print("dic info autre fichier >>>  ", dic_info[name_file])
        b = deserialize_players(dic_info, dic_players, name_file)
        deserialize_tournement(dic_info, name_file, b, None, None)
        print("lloooppppp ", dic_info[name_file].name)
        print("tttttt ", dic_info[name_file].players)


    if i >= 2:

        viewtable.display_start_time(name_round)
        list_new_match = utils.new_round(players_ranks, pairs_matched)
        viewtable.display_table_round(list_new_match, name_round)
        matches = name_round.matches
        utils.get_matches(list_new_match, dic_players, matches)
        dic_info[name_file].rounds.append(name_round.return_dic_round())
        score_sorted = utils.get_score_sorted(name_round)
        players_ranks = utils.create_ranking(name_round, score_sorted)
        viewtable.display_end_time(name_round)
        dic_rank = info.sorted_players(dic_players, players_ranks)
        viewtable.display_table_tournament(dic_rank)
        print("nbr de round  ", int(dic_info[name_file].nbr_rounds))
        print("lloooppppp 2222 ", dic_info[name_file].name)
        print("tttttt 222222  ", dic_info[name_file].players)
        #viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, name_file)
        dic_info = viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file, "lola")
        name_file = 'lola'
        print("dic info autre fichier >>>  ", dic_info[name_file])
        dic_info[name_file].players = info.check_players(dic_players)

print("\n")
print("Le gagnant est  :  ", players_ranks[0])
