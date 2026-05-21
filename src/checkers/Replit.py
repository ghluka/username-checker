"""https://repl.it/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://replit.com/@"

    @BaseChecker.check.register
    def _(self, username:str, proxies:str="") -> str|None:
        proxies = self.get_proxy(proxies)

        if not 2 < len(username) <= 15:
            return None
        elif "--" in username:
            return None
        elif not all(c.isalnum() and c.isascii() or c in "-" for c in username):
            return None

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=proxies) as client:
                r = client.head(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.status_code == 404 else None
