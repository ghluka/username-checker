"""https://roblox.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://auth.roblox.com/v1/usernames/validate?birthday=2000-01-01T00:00:00.000Z&context=Signup&username="

    @BaseChecker.check.register
    def _(self, username:str, proxies:str="") -> str|None:
        proxies = self.get_proxy(proxies)

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.json().get('code') == 0 else None
