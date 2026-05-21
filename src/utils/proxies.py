"""Proxy utils.
"""
import httpx
from colorama import Fore


def test_proxy(proxy:str) -> bool:
    """Tests the validity of a proxy."""
    proxies = {"http://":f"{proxy}", "https://":f"{proxy}"}

    try:
        with httpx.Client(verify=False, proxies=proxies) as client:
            _ = client.get("https://httpbin.io/ip").json()
            return True
    except:
        return False


def get_proxy(proxies:list) -> dict:
    """Gets a valid proxy from a list of proxies."""
    for proxy in proxies:
        proxies.remove(proxy)
        proxy = proxy.removesuffix("\n")
        if test_proxy(proxy):
            return {"http://":f"{proxy}", "https://":f"{proxy}"}

    print(f"{Fore.RED}No valid proxy in your provided list! Make sure you're using HTTP proxies and not SOCK5.{Fore.RESET}")
    exit(1)


if __name__ == "__main__":
    test = "".splitlines() # put an IP to test there
    print(get_proxy(test))
