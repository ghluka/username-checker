"""https://kahoot.it/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://create.kahoot.it/rest/users/usernameavailable"

    @BaseChecker.check.register
    def _(self, username:str, proxies:str="") -> str|None:
        proxies = self.get_proxy(proxies)

        headers={"x-kahoot-user-identifier": username}

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=proxies) as client:
                r = client.get(self.ENDPOINT, headers=headers)
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.json().get("isUsernameAvailable") else None
