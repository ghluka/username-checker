"""https://kahoot.it/
"""
import time

import httpx

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://create.kahoot.it/rest/users/usernameavailable"

    def check(self, username: str, proxies: str = "") -> str | None:
        proxy = self.get_proxy(proxies)
        mounts = self.build_mounts(proxy) if proxy else None

        headers = {"x-kahoot-user-identifier": username}

        while True:
            try:
                with httpx.Client(verify=False, mounts=mounts, timeout=10.0) as client:
                    r = client.get(self.ENDPOINT, headers=headers)
            except (httpx.ProxyError, httpx.ConnectError, httpx.TimeoutException):
                return None

            if r.status_code != 429:
                break
            time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.json().get("isUsernameAvailable") else None
