from model.tournament import Tournament
from model.player import Player
from model.round import Round
import controller.utils
import controller.info
from view.v_table import ViewTable
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
        p = Player(p_name, p_first_name, p_d_o_b, p_sex)
        dic_players["joueur_" + str(i)] = p
    return dic_players


def create_info_tournament():
    name = input("Nom du tournoi: ")
    place = input("Lieu du tournoi: ")
    date = input("Date du tournoi: ")
    #t_c = info.check_time_control()
    t_c = input("time controle: ")
    players = info.check_players(create_players())
    nbr_rounds = info.check_nbr_round()
    desc = input("Description du tournoi ")
    t = Tournament(name, place, date, nbr_rounds, t_c, players, desc)
    dic_info[name] = t

    return dic_info


create_info_tournament()

name_tournament = list(dic_info.keys())[0]
db_file = viewmenu.create_name_file(name_tournament)

viewmenu.display_menu(dic_info, db_file)

viewtable.display_table_tournament(dic_players)

nbr_rounds = int(dic_info[name_tournament].nbr_rounds)
rounds = dic_info[name_tournament].rounds
pairs_matched = dic_info[name_tournament].pairs_matched
players = dic_info[name_tournament].players


for nbr in range(nbr_rounds):
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
        rounds.append(name_round.return_dic_round())
        viewtable.display_end_time(name_round)
        players = info.check_players(dic_players)
        dic_rank = info.sorted_players(dic_players, players_ranks)
        viewtable.display_table_tournament(dic_rank)
        viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file)

    if i >= 2:
        viewtable.display_start_time(name_round)
        list_new_match = utils.new_round(players_ranks, pairs_matched)
        viewtable.display_table_round(list_new_match, name_round)
        matches = name_round.matches
        utils.get_matches(list_new_match, dic_players, matches)
        rounds.append(name_round.return_dic_round())
        score_sorted = utils.get_score_sorted(name_round)
        players_ranks = utils.create_ranking(name_round, score_sorted)
        viewtable.display_end_time(name_round)
        dic_rank = info.sorted_players(dic_players, players_ranks)
        viewtable.display_table_tournament(dic_rank)
        viewmenu.display_menu_all(dic_info, dic_players, dic_rank, db_file)
        players = info.check_players(dic_players)

print("\n")
print("Le gagnant est  :  ", players_ranks[0])
