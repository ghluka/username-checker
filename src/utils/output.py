"""Output utils.
"""
import os

from colorama import Fore


def clear() -> None:
    """Clears screen"""
    os.system("cls" if os.name == "nt" else "clear")


def title() -> None:
    """Outputs title as ASCII art"""
    print(
        Fore.CYAN + \
        "  ██    ██  █████   ██████ \n" \
        "  ██    ██ ██   ██ ██      \n" \
        "  ██    ██ ███████ ██      \n" \
        "  ██    ██ ██   ██ ██      \n" \
        "   ██████  ██   ██  ██████ \n" \
        + Fore.BLUE + \
        "Username Availability Checker" + "\n" \
        + Fore.RESET
    )


def print_columns(values:list, columns:int=3, start:str="", end:str="\n") -> None:
    """Outputs list in columns"""
    out = start
    seperator = len(max(values, key=len))

    for i, value in enumerate(values, 1):
        out += f"{value: <{seperator}}"
        out += f"\n{start}" if i % columns == 0 else "    "

    print(out, end=end)


if __name__ == "__main__":
    clear()
    title()
    print_columns(["a", "b", "c", "d", "e", "F", "g", "H"])
