"""https://solo.to/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://api.solo.to/"

    @BaseChecker.check.register
    def _(self, username:str, proxies:str="") -> str|None:
        proxies = self.get_proxy(proxies)

        if not (1 < len(username) <= 20):
            return None
        elif username.endswith(".") or username.endswith(".") or ".." in username:
            return None
        elif not all(c.isalnum() and c.isascii() or c in "-_." for c in username):
            return None

        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}", headers=headers)
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)

        return username if "page not found" in r.text else None
