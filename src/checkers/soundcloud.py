"""https://soundcloud.com/
"""
import time

import httpx

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://soundcloud.com/"

    def check(self, username: str, proxies: str = "") -> str | None:
        proxy = self.get_proxy(proxies)

        if not 3 < len(username) <= 25:
            return None
        elif username.startswith("-") or username.startswith("_"):
            return None
        elif username.endswith("-") or username.endswith("_"):
            return None
        elif not all(c.isalnum() and c.isascii() or c in "-_" for c in username):
            return None

        mounts = self.build_mounts(proxy) if proxy else None

        while True:
            try:
                with httpx.Client(verify=False, mounts=mounts, timeout=10.0) as client:
                    r = client.head(f"{self.ENDPOINT}{username}")
            except (httpx.ProxyError, httpx.ConnectError, httpx.TimeoutException):
                return None

            if r.status_code != 429:
                break
            time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.status_code == 404 else None
