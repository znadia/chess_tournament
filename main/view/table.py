from rich.console import Console
from rich.table import Table
from operator import itemgetter


console = Console()


class ViewTable:
    def display_table_tournament(self, players):
        # Affiche tout sur les joueurs
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Joueurs")
        table.add_column("Nom et Prénom", style="dim", width=20)
        table.add_column("Classement")
        table.add_column("Score")
        for player in players:
            table.add_row(
                player,
                f"{players[player].first_name} {players[player].name}",
                f"{players[player].ranking}",
                f"{players[player].score}",
            )
        console.print(table)

    def display_table_round(self, players, name_round, name_file):
        # Affiche les matches qui vont etre joués
        table = Table(show_header=True, header_style="bold magenta")
        name_tournament = name_file + ": " + name_round.name
        table.add_column(name_tournament)

        for player in players:
            table.add_row(f"{player[0]} vs {player[1]}")
        console.print(table)

    def display_start_time(self, name_round):
        # Affiche l'heure du début
        name_round.start_time = name_round.get_times()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column(" Début du round ")
        table.add_row(name_round.start_time)
        console.print(table)

    def display_end_time(self, name_round):
        # Affiche l'heure de fin
        name_round.end_time = name_round.get_times()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column(" Fin du round ")
        table.add_row(name_round.end_time)
        console.print(table)

    def display_round_match(self, rounds):
        # Affiche le rapport des rounds et matches
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Rounds")
        table.add_column("Match")
        table.add_column("Joueurs")

        for r in rounds:
            for match in r.get("matches"):
                table.add_row(
                    f"{r.get('name_round')}",
                    f"{match.get('name_match')}",
                    f"{match.get('match_played')}",
                )
        console.print(table)

    def display_tournement(self, tournement):
        # Affiche tout les tournois
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Tournois")
        for file in tournement:
            table.add_row(f"{file}")
        console.print(table)

    def display_all_player(self, data, n_file, option):
        # Affiche tout les acteurs des tournois
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Nom et Prénom", style="dim", width=20)
        table.add_column("Classement")
        table.add_column("Score")

        player = []
        for datas in data:
            for i in datas:
                player.append(datas[i])
        for x in sorted(player, key=itemgetter(option)):
            table.add_row(
                f"{x['name']} {x['first_name']}",
                f"{x['ranking']}",
                f"{x['score']}",
            )
        console.print(table)
