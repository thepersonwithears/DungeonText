from rich.prompt import Confirm
from rich.console import Console
from rich.panel import Panel
from dungeontext_lib import Clear

console = Console()
console.print(Panel.fit("[red]DungeonText!", style="italic"))
# ^ Add a panel for the information like commands

if Confirm.ask("Would you like to start a new game?"):
    Clear()
    console.print("Starting a new game...")
