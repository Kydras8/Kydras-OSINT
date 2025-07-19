#!/usr/bin/env python3

import requests

print("🔎 Kydras Username Quick Checker")
username = input("Enter username to check: ")

sites = {
    "GitHub": f"https://github.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}/",
    "Twitter": f"https://twitter.com/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}/"
}

for site, url in sites.items():
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Found on {site}: {url}")
        else:
            print(f"[-] Not found on {site}")
    except requests.RequestException:
        print(f"[!] Error connecting to {site}")
