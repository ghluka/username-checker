"""https://speedrun.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://www.speedrun.com/api/v2/PutAuthSignup"

    @BaseChecker.check.register
    def _(self, username:str, proxies:str="") -> str|None:
        proxies = self.get_proxy(proxies)

        payload = {"areaId": "", "email": "email@example.com", "name": username, "password": "realpassword123"}

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=proxies) as client:
                r = client.post(self.ENDPOINT, json=payload)
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.status_code == 200 else None
