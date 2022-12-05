import view.info
from model.player import Player
from model.tournament import Tournament

info = view.info


def create_players():
    # Crée les instances des joueurs
    dic_players = {}
    create_players = {}

    x = 1
    while x <= 8:
        p_name = input("Nom: ")
        p_first_name = input("Prénom: ")
        p_d_o_b = info.int_date_birthday()
        p_sex = info.check_sex()
        p_rank = info.check_ranking()
        p = Player(p_name, p_first_name, p_d_o_b, p_sex, p_rank, 0)
        key = p_rank
        if key == "0":
            create_players[str(p_name)] = p
        else:
            create_players[str(p_rank)] = p
        x += 1

    create_players = dict(sorted(create_players.items()))
    print(create_players)

    i = 1
    for player in create_players:
        print("i = ", i)
        print("player = ", player)
        dic_players["joueur_" + str(i)] = create_players[player]
        i += 1

    return dic_players


def create_info_tournament():
    # Crée l'instance d'un tournoi
    dic_info = {}

    name = input("Nom du tournoi: ")
    place = input("Lieu du tournoi: ")
    date = input("Date du tournoi: ")
    t_c = info.check_time_control()
    dic_players = create_players()
    players = check_players(dic_players)
    nbr_rounds = info.check_nbr_round()
    desc = input("Description du tournoi ")
    t = Tournament(name, place, date, nbr_rounds, t_c, players, [], desc, [])
    dic_info[name] = t

    return dic_info, dic_players


def check_players(dic_players):
    # Convertie un dictionnaire en liste
    list_data = []

    for key, var in dic_players.items():
        a = {key: var.return_players()}
        list_data.append(a)
    return list_data


def change_rank(dic_players):
    # Change le classement des joueurs
    for k, v in dic_players.items():
        print(k)
        v.ranking = input("Classement du: ")
