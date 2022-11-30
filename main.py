from model.round import Round
import controller.tournament
import controller.player
import controller.utils
import controller.deserialize
from view.table import ViewTable
from view.menu import ViewMenu


viewtable = ViewTable()
viewmenu = ViewMenu()
tournament = controller.tournament
player = controller.player
utils = controller.utils
deserialize = controller.deserialize

info, p = viewmenu.display_start_menu()

if p == 1:
    dic_info = info
    name_file = list(dic_info.keys())[0]
    db_file = viewmenu.create_name_file(name_file)
    dic_players = deserialize.players(dic_info, name_file)
    dic_info = deserialize.tournement(dic_info, name_file, dic_players)
    nbr = len(dic_info[name_file].rounds) + 1

else:
    dic_info = info
    dic_players = p
    name_file = list(dic_info.keys())[0]
    db_file = viewmenu.create_name_file(name_file)
    nbr = 1

dic_info, new = viewmenu.display_menu_all(dic_info, dic_players, db_file)

pairs_matched = dic_info[name_file].pairs_matched
while nbr <= (int(dic_info[name_file].nbr_rounds)):
    name_round = "round_" + str(nbr)
    name_round = Round(name=name_round, all_players=dic_players)
    if nbr == 1:
        # Déroulement d'un Round/Matches
        viewtable.display_start_time(name_round)
        name_round.first_round()
        pairs_matched.extend(name_round.first_round())
        viewtable.display_table_round(pairs_matched, name_round, name_file)
        utils.get_matches(pairs_matched, dic_players, name_round.matches)
    if nbr >= 2:
        score_sorted = player.list_score_sorted(name_round)
        players_ranks = player.players_ranking(dic_players, score_sorted)
        viewtable.display_start_time(name_round)
        pairs_matched = dic_info[name_file].pairs_matched
        list_new_match = utils.new_round(players_ranks, pairs_matched)
        viewtable.display_table_round(list_new_match, name_round, name_file)
        utils.get_matches(list_new_match, dic_players, name_round.matches)

    viewtable.display_end_time(name_round)
    dic_info[name_file].rounds.append(name_round.return_dic_round())
    dic_info[name_file].players = tournament.check_players(dic_players)
    dic_info, new = viewmenu.display_menu_all(dic_info, dic_players, db_file)
    if new == 1:
        name_file = list(dic_info.keys())[0]
        db_file = viewmenu.create_name_file(name_file)
        dic_players = deserialize.players(dic_info, name_file)
        dic_info = deserialize.tournement(dic_info, name_file, dic_players)
        nbr = len(dic_info[name_file].rounds)

    nbr += 1


dic_info[name_file].end = True
viewmenu.the_end(dic_info, db_file)
viewtable.display_table_tournament(dic_players)

print("\n")
print("|############################################################|")
print("|                             FIN                            |")
print("|############################################################|")
