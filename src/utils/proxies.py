from collections.abc import Iterable

import httpx
from colorama import Fore

TEST_URL = "https://httpbin.io/ip"
TIMEOUT = 5.0


def build_mounts(proxy: str) -> dict:
    transport = httpx.HTTPTransport(proxy=proxy)

    return {
        "http://": transport,
        "https://": transport,
    }


def test_proxy(proxy: str) -> bool:
    proxy = proxy.strip()

    try:
        with httpx.Client(
            mounts=build_mounts(proxy),
            timeout=TIMEOUT,
            verify=False,
        ) as client:

            response = client.get(TEST_URL)
            response.raise_for_status()

            return True

    except (
        httpx.ConnectError,
        httpx.ProxyError,
        httpx.TimeoutException,
        httpx.HTTPStatusError,
    ):
        return False


def get_proxy(proxies: Iterable[str]) -> str:
    for proxy in map(str.strip, proxies):

        if test_proxy(proxy):
            return proxy

    raise RuntimeError(
        f"{Fore.RED}"
        "No valid proxy found! "
        "Ensure the proxies are alive and correctly formatted."
        f"{Fore.RESET}"
    )


if __name__ == "__main__":

    proxies = [
        "http://127.0.0.1:8080",
        "socks5h://127.0.0.1:9050",
    ]

    print(get_proxy(proxies))
