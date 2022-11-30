def list_score_sorted(name_round):
    # Récupère le score du joueur sous forme de liste
    list_score = []
    for k in name_round.all_players.keys():
        value = name_round.all_players[k].score
        list_score.append(value)
    sort_list = sorted(list_score, reverse=True)
    return sort_list


def find_key(v, dic_players):
    # Récupère la clef d'une valeur
    for k, val in dic_players.items():
        if v == val.score:
            return k


def players_ranking(players, score_sorted):
    # Crée une liste trier des clefs par score
    players_cop = players.copy()
    player_ranked = []
    for score in score_sorted:
        k = find_key(score, players_cop)
        player_ranked.append(k)
        del players_cop[k]
    return player_ranked


def list_rank_sorted(players):
    # Récupère le classement du joueur sous forme de liste
    list_ranks = []
    for k in players.keys():
        value = players[k].ranking
        list_ranks.append(value)
    sort_list = sorted(list_ranks)
    return sort_list


def find_rank(v, dic_players):
    # Récupère la clef d'une valeur
    for k, val in dic_players.items():
        if v == val.ranking:
            return k


def rank_player(players, score_sorted):
    # Crée une liste trier des clefs par classement
    players_cop = players.copy()
    player_ranked = []
    for score in score_sorted:
        k = find_rank(score, players_cop)
        player_ranked.append(k)
        del players_cop[k]
    return player_ranked


def list_name_sorted(players):
    # Récupère le nom du joueur sous forme de liste
    list_name = []
    for k in players.keys():
        value = players[k].name
        list_name.append(value)
    sort_list = sorted(list_name)
    return sort_list


def find_name(v, dic_players):
    # Récupère la clef d'une valeur
    for k, val in dic_players.items():
        if v == val.name:
            return k


def name_player(players, score_sorted):
    # Crée une liste trier des clefs par nom
    players_cop = players.copy()
    player_name = []
    for score in score_sorted:
        k = find_name(score, players_cop)
        player_name.append(k)
        del players_cop[k]
    return player_name


def sorted_players(player, attribut):
    # Crée un dictionnaire trié des joueurs en fonction
    # du classement ou du nom ou
    if attribut == "ranking":
        value = list_rank_sorted(player)
        list_players = rank_player(player, value)
    if attribut == "name":
        value = list_name_sorted(player)
        list_players = name_player(player, value)
    dic_sorted = {}
    for key in list_players:
        dic_sorted[key] = player[key]
    return dic_sorted
