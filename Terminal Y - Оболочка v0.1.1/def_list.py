import configparser   
from rich import *
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import os
file_updater = "update.sysY"

def analys(command, debug_mode):
    if command == 'exit':
        exit()
    if command == 'update':
        if os.path.exists(file_updater) == True:
           config = configparser.ConfigParser()
           config.read("update.sysY")
           print(config["'' - Updater file - ''"]["file_update_main"]) 
           print(config["'' - Updater file - ''"]["file_update_def_list"])
           return command
        else:
            print('Простите файл обновления не существует, проверьте наличие файла в корневой папке')
            input('Нажмите Enter для продолжения>>  ')
            return command

    if command == 'help':
        print("[cyan] ---  help - see all the commands and their descriptions\n",
        "[cyan]---  update - update the terminal to the latest version\n",
        "[cyan]---  ",)
        return command
    
    if command == ':debug:':
        if debug_mode == True:
            debug_mode = False
            print('debug mode = False')
        else:
            print('debug mode = True')
            print('[red]all debug commands visible[/red]')
            debug_mode = True
            print(debug_mode)

