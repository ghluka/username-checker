"""https://lichess.org/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://lichess.org/api/player/autocomplete?term="

    @BaseChecker.check.register
    def _(self, username:str, proxies:str="") -> str|None:
        proxies = self.get_proxy(proxies)

        payload = f"{username}&exists=1"

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=proxies) as client:
                r = client.get(f"{self.ENDPOINT}{payload}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.text == "false" else None
