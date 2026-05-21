"""User menu for checking username availability.
"""
import concurrent.futures
import itertools
import pathlib
import time

from colorama import Fore

from utils.checkers import get_checker, path
from utils.output import clear, title
from utils.prompts import bool_input, select_checker, select_file


def main():
    """
    Prompts the user for username data and saves the hits as a file. 
    """
    clear()
    title()
    try:
        # Service selector
        checker_name = select_checker()
        print(f"\nSelected {Fore.CYAN}{checker_name.capitalize()}{Fore.RESET}.")
        checker = get_checker(checker_name)

        # Username list selector
        print(f"\n{Fore.BLUE}>{Fore.RESET} Select your usernames list.")
        usernames = select_file()
        print(f"Selected {Fore.CYAN}{len(usernames)}{Fore.RESET} usernames from list.")

        # Proxy selector
        proxies = []
        if bool_input("\nUse proxies?", False):
            print(f"{Fore.BLUE}>{Fore.RESET} Select your proxy list.")
            proxies = select_file()
            print(f"Loaded {Fore.CYAN}{len(proxies)}{Fore.RESET} proxies.")

        # Get hits
        print("\nStarting...")
        start = time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            hits = set(executor.map(checker.check, usernames, itertools.repeat(proxies)))
        if None in hits:
            hits.remove(None)

        elapsed = time.perf_counter() - start
        print(f"{Fore.CYAN}Done!{Fore.RESET} Took {elapsed:.2f}s")

        # Save hits
        pathlib.Path(f"{path}/hits").mkdir(exist_ok=True)
        output_name = f"{checker_name.lower()}-{time.strftime('%Y%m%d-%H%M%S')}"
        with open(f"{path}/hits/{output_name}.txt", "w", encoding="utf8") as f:
            f.writelines("\n".join(hits))

    except (KeyboardInterrupt, EOFError):
        pass

    print("\nGoodbye!")


if __name__ == "__main__":
    main()
