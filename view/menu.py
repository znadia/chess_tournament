import database
import inquirer

class ViewMenu:


    def display_start_menu(self):
        
        questions = [
            inquirer.List(
                "size",
                message="Que voulez-vous faire ?",
                choices=["Créer un tournoi", "Quitter"],
            ),
        ]
        answers = inquirer.prompt(questions)
        print(answers["size"])
        if answers["size"] == "Quitter":
            print("Au revoir")
            quit()


    def create_name_file(self, name_tournament):
        return database.create_db_file(name_tournament)

#########################################################################################

    def display_report(self, dic_tournement, player, rank, db):

        questions = [
            inquirer.List(
                "size",
                message="Quel rapport voulez-vous visualiser ?",
                choices=["Joueurs", "Rounds/Matches", "Menu précédent"],
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
                print(player)
        
            if answers["size"] == "Par classement":
                print(rank)
    
        
        if answers["size"] == "Rounds/Matches":
            print(round)
    
#########################################################################################

    def display_menu(self, tournement, db):
        questions = [
            inquirer.List(
                "size",
                message="Que voulez-vous faire ?",
                choices=["Sauvegarder les informations", "Continuer", "Quitter"],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["size"] == "Sauvegarder les informations":
            database.insert_db_info(tournement, db)


        if answers["size"] == "Quitter":
            print("Au revoir")
            quit()

#########################################################################################

    def display_menu_all(self, tournement, player, rank, db, name_file):
        questions = [
            inquirer.List(
                "size",
                message="Que voulez-vous faire ?",
                choices=["Sauvegarder les informations", "Continuer", "Visualiser les rapport", "Reprendre un tournoi","Quitter"],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["size"] == "Sauvegarder les informations":
            database.add_data(tournement, db)
            print("L'enregistrement a été effectué avec succès.")
          
        if answers["size"] == "Visualiser les rapport":
            self.display_report(tournement, player, rank, db)
        
        if answers["size"] == "Reprendre un tournoi":
            return database.open_db(name_file)


        if answers["size"] == "Quitter":
            print("Au revoir")
            quit()

