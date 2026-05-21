# 📛 Username Availability Checker
Checks if usernames are available on a bunch of websites.

[![GitHub license](https://img.shields.io/github/license/ghluka/username-availability-checker)](LICENSE)

> [!WARNING]  
> However unlikely, most if not all services serve the right to ban you from using their service for abusing their API. **Use this at your own risk.** I am not liable for any problems/consequences that may arise from using this program. This program solely serves as a proof of concept.

## ⚙️ Running

Simply install all the requirements and run the main script!

```sh
# Install dependencies
$ pip install -r requirements.txt

# Run main script
$ python3 main.py
```

## 📃 Supported websites <!-- Websites start -->[13 total]

- [Chess.com](https://chess.com/)
- [Github](https://github.com/)
- [Kahoot](https://kahoot.it/)
- [Lichess](https://lichess.org/)
- [Linktree](https://linktr.ee/)
- [Minecraft](https://minecraft.net/)
- [Replit](https://repl.it/)
- [Roblox](https://roblox.com/)
- [Solo.to](https://solo.to/)
- [Soundcloud](https://soundcloud.com/)
- [Speedrun.com](https://speedrun.com/)
- [Steam](https://soundcloud.com/)
- [Twitch](https://twitch.tv/)

<!-- Websites end -->

## 🖇️ Proxy support

We allow the use of proxies, however, if you use public proxies you'll likely encounter an infinite ratelimit from hundreds or thousands of people using the same proxy. Proxies can dramatically speed up or slow down the process depending on their quality.

Proxies should be stored in a format in a `protocol://ip:port` format.