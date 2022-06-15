
from Model.player import Player
import random

list_players = []

def create_players():

    for i in range(8):
        p_name = input("ton nom? ")
        p_first_name = input("ton prénom? ")
        p_d_o_b = int(input("Date de naissance? "))
        p_sex = input("Homme ou Femme? ")
        p = Player(p_name,p_first_name, p_d_o_b, p_sex)
        list_players.append(p)

create_players()

print(list_players)
print(list_players[1].name)

print("\n")

print(random.choices(list_players, k=2))



