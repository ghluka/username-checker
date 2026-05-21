# 📛 Username Availability Checker
Checks if usernames are available on a bunch of websites.

[![GitHub license](https://img.shields.io/github/license/ghluka/username-checker)](LICENSE)

> [!WARNING]  
> Most services serve the right to ban you from using their service for abusing their API. Use this at your own risk, make sure you have read the ToS of the supported websites and understand before using.

## ⚙️ Running

Simply install all the requirements and run the main script!

```sh
$ cd src

# Install dependencies
$ pip install -r requirements.txt

# Run main script
$ python3 main.py
```

## 📃 Supported websites

- [Chess.com](https://chess.com/)
- [Github](https://github.com/)
- [Kahoot](https://kahoot.it/)
- [Lichess](https://lichess.org/)
- [Linktree](https://linktr.ee/)
- [Minecraft](https://minecraft.net/)
- [Replit](https://repl.it/)
- [Roblox](https://roblox.com/)
- [Soundcloud](https://soundcloud.com/)
- [Steam](https://soundcloud.com/)

## 🖇️ Proxy support

Proxies should be stored in a format in a `protocol://ip:port` format, for example:

```
http://127.0.0.1:8080
socks5h://127.0.0.1:9050
```
