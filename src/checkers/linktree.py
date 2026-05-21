"""https://linktr.ee/
"""
import time

import httpx

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://linktr.ee/validate/username"

    def check(self, username: str, proxies: str = "") -> str | None:
        proxy = self.get_proxy(proxies)
        mounts = self.build_mounts(proxy) if proxy else None

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}
        payload = {"username": username, "returnSuggestions": False}

        while True:
            try:
                with httpx.Client(verify=False, mounts=mounts, timeout=10.0) as client:
                    r = client.post(self.ENDPOINT, json=payload, headers=headers)
            except (httpx.ProxyError, httpx.ConnectError, httpx.TimeoutException):
                return None

            if r.status_code != 429:
                break
            time.sleep(self.RATELIMIT_TIMEOUT)

        return username if r.json()["result"] == "success" else None
