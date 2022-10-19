from rich.console import Console
from rich.table import Table

console = Console()

class ViewClass:


    def display_table_tournament(self, players):
        
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

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column(name_round.name)

        for player in players:
            table.add_row(f"{player[0]} vs {player[1]}")
        console.print(table)


    def display_time(self, a, name_round):
        
        if a == "start_time":
            name_round.start_time = name_round.get_times()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column(" Début du round ")
            table.add_row(name_round.start_time)
            console.print(table)

        if a == "end_time":
            name_round.end_time = name_round.get_times()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column(" Fin du round ")
            table.add_row(name_round.end_time)
            console.print(table)