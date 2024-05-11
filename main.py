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


for root, dirs, files in os.walk("Cards"):
    for data in files:
        if data == "data.json":
            with open(os.path.join(root, data), "r") as f:
                data = json.load(f)
                print(f"Processing {data['bank']['native_name']}...")
                for l in data["cards"]:
                    issuer = data["bank"]
                    if l.get("filename") is None:
                        image = f'https://raw.githubusercontent.com\\HarukaKinen\\Cardentify\\main\\{os.path.join(root, l["description"])}.{l["ext"]}'
                        path = f'https://github.com\\HarukaKinen\\Cardentify\\blob\\main\\{os.path.join(root, l["description"])}.{l["ext"]}'
                    else:
                        image = f'https://raw.githubusercontent.com\\HarukaKinen\\Cardentify\\main\\{os.path.join(root, l["filename"])}'
                        path = f'https://github.com\\HarukaKinen\\Cardentify\\blob\\main\\{os.path.join(root, l["filename"])}'
                    l.update({"image": image, "url": path, "issuer": issuer})
                    cards.append(l)
                    banks.append(issuer)

country_counts = Counter([bank["country"] for bank in banks])
banks = sorted(banks, key=lambda x: x["english_name"])
banks = sorted(banks, key=lambda x: (-country_counts[x["country"]], x["country"]))

if banks:
    with open("bank.json", "w") as f:
        json.dump(banks, f, indent=4)

cards = sorted(cards, key=lambda x: x["description"])
cards = sorted(cards, key=lambda x: x["issuer"]["english_name"])
cards = sorted(cards, key=lambda x: x["card"]["country"])

with open("data.json", "w") as f:
    json.dump(cards, f, indent=4)
