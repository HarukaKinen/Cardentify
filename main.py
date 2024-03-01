import os
import requests
import json
from collections import Counter

TOKEN = os.environ.get("TOKEN")

repo = "HarukaKinen/Cardentify"

r = requests.get(
    f"https://api.github.com/repos/{repo}/contents/Cards",
    headers={"Authorization": f"Bearer {TOKEN}"},
)
repos = r.json()

cards = []

banks = []

for bank in repos:
    if bank["type"] == "dir":
        path = bank["path"]
        name = bank["name"]
        print(f"Processing {name}")
        r = requests.get(bank["url"])
        card_data = r.json()
        for i in card_data:
            if i["name"] == "data.json":
                r = requests.get(i["download_url"])
                data = r.json()
                for l in data["cards"]:
                    issuer = data["bank"]
                    if l.get("filename") is None:
                        image = f'{i["download_url"].replace("data.json", l["description"])}.{l["ext"]}'
                        path = f'{i["html_url"].replace("data.json", l["description"])}.{l["ext"]}'
                    else:
                        image = f'{i["download_url"].replace("data.json", l["filename"])}'
                        path = f'{i["html_url"].replace("data.json", l["filename"])}'
                    l.update({"image": image, "url": path, "issuer": issuer})
                    cards.append(l)
                    banks.append(issuer)

country_counts = Counter([bank['country'] for bank in banks])
banks = sorted(banks, key=lambda x: x['english_name'])
banks = sorted(banks, key=lambda x: (-country_counts[x['country']], x['country']))

if banks:
    with open("bank.json", "w") as f:
        json.dump(banks, f, indent=4)

cards = sorted(cards, key=lambda x: x["issuer"]["english_name"])
cards = sorted(cards, key=lambda x: x["card"]["country"])

with open("data.json", "w") as f:
    json.dump(cards, f, indent=4)
