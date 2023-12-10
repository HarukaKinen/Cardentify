import os
import requests
import json

TOKEN = os.environ.get("TOKEN")

repo = "HarukaKinen/Cardentify"

r = requests.get(f"https://api.github.com/repos/{repo}/contents/Cards", headers={"Authorization": f"Bearer {TOKEN}"})
repos = r.json()

cards = []

for files in repos:
    if files["name"] == "bank.json":
        r = requests.get(files["download_url"])
        bank_data = r.json()
        bank_data = sorted(bank_data, key=lambda x: x['code'])
    if files["type"] == "dir":
        r = requests.get(files["url"])
        cards_data = r.json()
        for card in cards_data:
            if card["type"] == "dir":
                path = card["path"]
                r = requests.get(card["url"])
                card_data = r.json()
                for i in card_data:
                    if i["name"] == "data.json":
                        r = requests.get(i["download_url"])
                        data = r.json()
                        for l in data:
                            image = i["download_url"].replace("data.json", l["card"]["image"])
                            path = i["html_url"].replace("data.json", l["card"]["image"])
                            l.update({"image": image, "url": path})
                            cards.append(l)

cards = sorted(cards, key=lambda x: x['issuer']['code'])

with open("data.json", "w") as f:
    json.dump(cards, f, indent=4)

if bank_data:
    with open("bank.json", "w") as f:
        json.dump(bank_data, f, indent=4)