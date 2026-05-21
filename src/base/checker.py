"""Base username availability checker class.
"""
from functools import singledispatchmethod

from utils.proxies import get_proxy


class BaseChecker:
    ENDPOINT = ""
    RATELIMIT_TIMEOUT = 0.5

    @singledispatchmethod
    def check(self) -> str|None:
        """Checks if username is available."""
        raise NotImplementedError

    def get_proxy(self, proxy_path:str) -> dict:
        """Returns a valid proxy."""
        if len(proxy_path) == 0:
            return {}
        return get_proxy(proxy_path)
