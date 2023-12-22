import def_list
from rich import *
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import os
console = Console()
debug_mode = False

command = 'a'

run_prog = True

print(Panel('[yellow]Terminal - Y[/yellow]\ncommands:\n' + '[cyan]---  help - see all the commands and their descriptions[/cyan]', title="[red]Welcome to the terminal[/red]"))

while(run_prog):
    command = input("T:// ")
    def_list.analys(command, debug_mode)
        


