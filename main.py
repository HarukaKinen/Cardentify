import os
import requests
import json

TOKEN = os.environ.get("TOKEN")

repo = "HarukaKinen/Cardentify"

r = requests.get(
    f"https://api.github.com/repos/{repo}/contents/Cards",
    headers={"Authorization": f"Bearer {TOKEN}"},
)
repos = r.json()

cards = []

for bins in repos:
    if bins["name"] == "bank.json":
        r = requests.get(bins["download_url"])
        bank_data = r.json()
    if bins["type"] == "dir":
        path = bins["path"]
        r = requests.get(bins["url"])
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

bank_data = sorted(bank_data, key=lambda x: x["english_name"])
bank_data = sorted(bank_data, key=lambda x: x["country"])

if bank_data:
    with open("bank.json", "w") as f:
        json.dump(bank_data, f, indent=4)

cards = sorted(cards, key=lambda x: x["issuer"]["english_name"])

with open("data.json", "w") as f:
    json.dump(cards, f, indent=4)
