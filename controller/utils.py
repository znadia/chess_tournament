from model.match import Match


def get_matches(list_match, dic_all_players, match):
    # Crée une instance match et ajoute le score
    
    for i in range(len(list_match)):
            players_match = list_match[i]
            i += 1
            name_match = "match_" + str(i)
            match_to_play = Match(name=name_match, players_pair=players_match)
            match_to_play.add_score_match(dic_all_players)
            match.append(match_to_play.return_dic_match())


def list_score_sorted(name_round):
    # Récupère le score du joueur sous forme de liste
    list_score = []
    for k in name_round.all_players.keys():
        value = name_round.all_players[k].score
        list_score.append(value)
    sort_list = sorted(list_score, reverse = True)
    return sort_list


def find_key(v, dic_players):
    # Récupère la clef d'une valeur 
    for k, val in dic_players.items(): 
        if v == val.score:
            return k


##################################
def create_ranking(name_round):

    score_sorted = list_score_sorted(name_round)
    # Crée une liste trier des clefs 
    players_cop = name_round.all_players.copy()
    player_ranked = []
    i = 1
    for score in score_sorted:
        k = find_key(score, players_cop)
        #name_round.all_players[k].ranking = i
        player_ranked.append(k)
        del(players_cop[k])
        i += 1
    return player_ranked

def sorted_players(dic_players, list_players):
    # Crée un dictionnaire trié des joueurs 
    dic_sorted = {}

    for key in list_players:
        dic_sorted[key] = dic_players[key]

    return dic_sorted


def check_match(list_match, player_1, player_2):
    # Check les matches passé
    sorted_player = sorted([player_1, player_2])
    if sorted_player in list_match:
        return False
    else:
        return sorted_player


def new_round(list_players, list_match):
    # Crée des nouveaux matches
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


