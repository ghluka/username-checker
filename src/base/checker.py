"""Base username availability checker class.
"""
from functools import singledispatchmethod

from utils.proxies import get_proxy


class BaseChecker:
    ENDPOINT = ""
    RATELIMIT_TIMEOUT = 0.5

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    )

    def check(self, username:str, proxies:str="") -> str|None:
        """Checks if username is available."""
        raise NotImplementedError

    def get_proxy(self, proxy_path:str) -> dict:
        """Returns a valid proxy."""
        if len(proxy_path) == 0:
            return {}
        return get_proxy(proxy_path)

    def build_mounts(self, proxy: str) -> dict:
        transport = httpx.HTTPTransport(proxy=proxy)

        return {
            "http://": transport,
            "https://": transport,
        }
