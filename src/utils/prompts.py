"""User prompts utils.
"""
import tkinter as tk
from tkinter import filedialog

from colorama import Fore

from utils.checkers import get_checkers, path
from utils.output import print_columns

root = tk.Tk()
root.wm_attributes('-topmost', 1)
root.withdraw()


def select_checker() -> str:
    """Outputs list of checkers and prompts user to select one."""
    checkers = get_checkers()
    print(f"Checkers ({len(checkers)}):")
    print_columns(checkers, start="  ", end="\n")

    name = input(f"{Fore.BLUE}>{Fore.RESET} Which checker do you want to use: ")
    while name.capitalize() not in checkers:
        print(f"{Fore.RED}Invalid checker! Try again.{Fore.RESET}\n")
        name = input(f"{Fore.BLUE}>{Fore.RESET} Which checker do you want to use: ")

    return name


def select_file() -> str:
    """Opens file dialog and prompts for text file. If cancelled, exits."""
    file = filedialog.askopenfilename(
        initialdir=f"{path}/presets",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file:
        exit()

    with open(file, encoding="utf8") as f:
        usernames = f.read().splitlines()

    return usernames


def bool_input(input_prompt:str, default:bool=True) -> bool:
    """Prompts user for a bool."""
    input_str = "\n" if input_prompt.startswith("\n") else ""
    input_prompt = input_prompt.lstrip("\n")
    input_str += f"{Fore.BLUE}>{Fore.RESET} {input_prompt} ({'Y/n' if default else 'y/N'}): "
    input_str = input(input_str)

    if input_str.lower().startswith("y"):
        return True

    elif input_str.lower().startswith("n"):
        return False

    return default
