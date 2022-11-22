import database
import inquirer
import os

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
        
        name_file = list(dic_tournement.keys())[0]

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
                print(dic_tournement[name_file].players)
        
            if answers["size"] == "Par classement":
                print(dic_tournement[name_file].players)
    
        
        if answers["size"] == "Rounds/Matches":
            print(dic_tournement[name_file].rounds)

        self.display_menu_all(dic_tournement, player, rank, db)

    
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


    def display_tournement(self):
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

        return database.open_db(answers['size'])



#########################################################################################

    def display_menu_all(self, dic_tournement, player, rank, db):
        questions = [
            inquirer.List(
                "size",
                message="Que voulez-vous faire ?",
                choices=["Sauvegarder les informations", "Continuer", "Visualiser les rapport", "Reprendre un tournoi","Quitter"],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["size"] == "Sauvegarder les informations":
            database.add_data(dic_tournement, db)
            print("L'enregistrement a été effectué avec succès.")
            self.display_menu_all(dic_tournement, player, rank, db)
          
        if answers["size"] == "Visualiser les rapport":
            self.display_report(dic_tournement, player, rank, db)
        
        if answers["size"] == "Reprendre un tournoi":
            return self.display_tournement(), True


        if answers["size"] == "Quitter":
            print("Au revoir")
            quit()

        return dic_tournement, None

