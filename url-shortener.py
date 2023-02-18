import pyshorteners
from pyperclip import copy
from pystyle import Write, Colors
Write.Print("Welcome To URL Shortener\n", Colors.baby_blue, interval=0.0025)
while True:
    url = Write.Input("Enter URL: ", Colors.dap_blue, interval=0.025)
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    copy( short_url)
    Write.Print(f"Shortened URL: {short_url}\nCopied short url to clipboard\n", Colors.dap_blue, interval=0.025)
    if url in ("exit", "quit", "q", "e"):
        Write.Print("Exiting...", Colors.baby_blue, interval=0.025)
        break
