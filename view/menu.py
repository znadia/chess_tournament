import os

import inquirer

import database
import controller.utils
import controller.tournament
from view.table import ViewTable

utils = controller.utils
tournament = controller.tournament
viewtable = ViewTable()


class ViewMenu:
    def display_start_menu(self):
        # Affichage du début
        questions = [
            inquirer.List(
                "size",
                message="Que voulez-vous faire ?",
                choices=["Créer un tournoi", "Reprendre un tournoi", "Quitter"],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["size"] == "Créer un tournoi":
            return tournament.create_info_tournament()

        if answers["size"] == "Reprendre un tournoi":
            try:
                return self.display_tournement(), 0
            except:
                print("Aucun tournoi enregistré\n")
                return self.display_start_menu()

        if answers["size"] == "Quitter":
            print("Au revoir")
            quit()

    def create_name_file(self, name_tournament):
        # Crée le fichier JSON
        if not ("data") in os.listdir():
            os.system("mkdir data")
        return database.create_db_file(name_tournament)


    def display_report(self, dic_tournement, player, db):
        # Affiche les rapports
        name_file = list(dic_tournement.keys())[0]
        questions = [
            inquirer.List(
                "size",
                message="Quel rapport voulez-vous visualiser ?",
                choices=["Joueurs", "Rounds/Matches", "Tournois", "Menu précédent"],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["size"] == "Joueurs":
            questions = [
                inquirer.List(
                    "size",
                    message="Veuillez faire un choix: ",
                    choices=["Par ordre alphabétique", "Par classement"],
                ),
            ]
            answers = inquirer.prompt(questions)

            if answers["size"] == "Par ordre alphabétique":
                viewtable.display_table_tournament(player)

            if answers["size"] == "Par classement":
                dic_rank = utils.sorted_players(player)
                viewtable.display_table_tournament(dic_rank)

        if answers["size"] == "Rounds/Matches":
            dic_r = dic_tournement[name_file].rounds
            viewtable.display_round_match(dic_r)

        if answers["size"] == "Tournois":
            files = os.listdir("data/")
            viewtable.display_tournement(files)

        return self.display_menu_all(dic_tournement, player, db)


    def display_tournement(self):
        # Affiche tout les tournois 
        db = []
        for file in os.listdir("data/"):
            db.append(file)
        questions = [
            inquirer.List(
                "size",
                message="Quel tournois voulez-vous reprendre ?",
                choices=db,
            ),
        ]
        answers = inquirer.prompt(questions)

        data = database.open_db(answers["size"])
        if data == False:
            return self.display_tournement()
        else:
            return data

    #########################################################################################

    def display_menu_all(self, dic_tournement, player, db):
        # Menu principal
        questions = [
            inquirer.List(
                "size",
                message="Que voulez-vous faire ?",
                choices=[
                    "Sauvegarder les informations",
                    "Continuer",
                    "Visualiser les rapport",
                    "Changer le classement",
                    "Reprendre un tournoi",
                    "Quitter",
                ],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["size"] == "Sauvegarder les informations":
            database.insert_db_info(dic_tournement, db)
            print("L'enregistrement a été effectué avec succès.")
            self.display_menu_all(dic_tournement, player, db)
            return dic_tournement, None

        if answers["size"] == "Continuer":
            return dic_tournement, None

        if answers["size"] == "Visualiser les rapport":
            self.display_report(dic_tournement, player, db)

        if answers["size"] == "Changer le classement":
            tournament.change_rank(player)
            return self.display_menu_all(dic_tournement, player, db)

        if answers["size"] == "Reprendre un tournoi":
            try:
                return self.display_tournement(), 1
            except:
                print("Aucun tournoi enregistré\n")
                return self.display_start_menu()

        if answers["size"] == "Quitter":
            print("Au revoir")
            quit()

    def the_end(self, dic_tournement, db):
        # Indique la fin du tournoi
        database.insert_db_info(dic_tournement, db)
