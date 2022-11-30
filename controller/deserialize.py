from model.tournament import Tournament
from model.player import Player


def players(dic_file, name_file):
    # deserialize les joueurs
    dic_players = {}
    for players in dic_file[name_file].get("players"):
        for key, value in players.items():
            p = []
            for v in value.values():
                p.append(v)
        pl = Player(p[0], p[1], p[2], p[3], p[4], p[5])
        dic_players[key] = pl

    return dic_players


def tournement(dic_info, name_file, obj_pl):
    # deserialize le tournoi
    x = []
    lst_r = dic_info[name_file].get("rounds")
    lst_m = dic_info[name_file].get("pairs_matched")
    for v in dic_info[name_file].values():
        x.append(v)
    t = Tournament(x[0], x[1], x[2], x[3], x[4], obj_pl, lst_m, x[7], lst_r)
    dic_info[name_file] = t

    return dic_info
