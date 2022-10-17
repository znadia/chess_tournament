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


    def display_table_round(self, players, name_of_round):

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column(name_of_round)

        for player in players:
            table.add_row(f"{player[0]} vs {player[1]}")

        console.print(table)
