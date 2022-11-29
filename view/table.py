from rich.console import Console
from rich.table import Table

console = Console()


class ViewTable:
    def display_table_tournament(self, players):
        # Affiche tout sur les joueurs
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Joueurs")
        table.add_column("Prénom", style="dim", width=12)
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

    def display_table_round(self, players, name_round):
        # Affiche les matches qui vont etre joués
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column(name_round.name)

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
        print(name_round.end_time)
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

        for k in rounds:
            for match in k.get("matches"):
                table.add_row(
                    f"{k.get('name_round')}",
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
