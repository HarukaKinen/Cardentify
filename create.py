from collections import OrderedDict
import json
import os

# [
#     {
#         "description": "原花旗超級紅利回饋鈦金卡",
#         "bin": [
#             540805
#         ],
#         "issuer": {
#             "native_name": "花旗銀行 (台灣)",
#             "english_name": "CITIBANK (TAIWAN)",
#             "country": "TW",
#             "url": "https://www.citibank.com.tw"
#         },
#         "manager": {
#             "native_name": "星展銀行 (台灣)",
#             "english_name": "DBS BANK (TAIWAN)",
#             "country": "TW",
#             "url": "https://www.dbs.com.tw"
#         },
#         "card": {
#             "image": "0.png",
#             "type": "Credit",
#             "brand": "MASTERCARD",
#             "level": "Infinite",
#             "country": "TW"
#         },
#         "source": "Apple Pay"
#     }
# ]

brands = {
    0: "UNKNOWN",
    1: "DINERS CLUB",
    2: "AMERICAN EXPRESS",
    3: "JCB",
    4: "VISA",
    5: "MASTERCARD",
    6: "UNION PAY",
    7: "DISCOVER",
    8: "MIR"
}

data = []

with open("Cards/bank.json", "r", encoding="UTF-8") as f:
    banks = json.load(f)

for key, value in brands.items():
    print(f"{key}: {value}")

print("Choose your card's brand: ", end="")

card_brand = int(input(""))

card_bin = input("Card Bin: ")

description = input("Description: ")

card_type = input("Type: ")

level = input("Level: ")

card_country = input("Country: ")

source = input("Source (Enter if Apple Pay): ")

if source == "":
    source = "Apple Pay"

img = input("Image ext (Enter if 0.png): ")

if img == "":
    img = "0.png"

bank_name = input("Issuer Bank: ")

issuer = ""

# print bank in bank list
for bank in banks:
    # if bank name in bank list, 模糊查找
    if bank_name.upper() in bank["english_name"] or bank_name in bank["native_name"]:
        print("Check your issuer bank: ")
        if bank["native_name"] == bank["english_name"]:
            print(f"- {bank['native_name']}")
        else:
            print(f"- {bank['native_name']} - {bank['english_name']}")
        print(f"- Country: {bank['country']}")
        print(f"- URL: {bank['url']}")
        print("Is this your issuer Bank? (y/n): ", end="")
        check = input("")
        if check == "y":
            issuer = bank
            break
        else:
            exit()

if issuer == "":
    print("Issuer Bank not found")
    exit()

manager_name = input("Manager Bank: ")

manager = ""

if manager_name != "":
    for bank in banks:
        if manager_name.upper() in bank["english_name"] or manager_name in bank["native_name"]:
            print("Check your manager bank: ")
            if bank["native_name"] == bank["english_name"]:
                print(f"- {bank['native_name']}")
            else:
                print(f"- {bank['native_name']} - {bank['english_name']}")
            print(f"- Country: {bank['country']}")
            print(f"- URL: {bank['url']}")
            print("Is this your issuer Bank? (y/n): ", end="")
            check = input("")
            if check == "y":
                manager = bank
                break
            else:
                exit()

if manager == "":
    print("Manager Bank not found")

print("Check your Card info: ")
print(f"Description: {description}")
print(f"BIN: {card_bin}")
print(f"Level: {level}")
print(f"Type: {card_type}")
print(f"Country: {card_country}")
print(f"Source: {source}")
print(f"Issuer Bank: {issuer['native_name']}")
print(f"Manager Bank: {manager['native_name']}")
print("Is this your Card info? (y/n): ", end="")
check = input("")
if check == "y":
    data.append({
        "description": description,
        "issuer": issuer,
        "card": {
            "image": "0.png",
            "type": card_type,
            "brand": brands[card_brand],
            "country": card_country
        },
        "source": source
    })

    if card_bin != "":
        data[0]["bin"] = [int(card_bin)]

    if manager_name != "":
        data[0]["manager"] = manager

    if level != "":
        data[0]["card"]["level"] = level

keys_order = ["description", "bin", "issuer", "manager", "card", "source"]

data = [OrderedDict(sorted(item.items(), key=lambda item: keys_order.index(item[0]))) for item in data]

# loop /Cards dir if didnt have "bin" foloder, create one

for dirs in os.listdir("Cards"):
    if dirs == card_bin:
        print(f"BIN {card_bin} already exist")
        # open data.json in bin folder and append data
        with open(f"Cards/{card_bin}/data.json", "r", encoding="UTF-8") as f:
            old_data = json.load(f)
        old_data.append(data[0])
        # save data as data.json in bin folder
        with open(f"Cards/{card_bin}/data.json", "w", encoding="UTF-8") as f:
            json.dump(old_data, f, indent=4, ensure_ascii=False)
        exit()
    else:
        os.mkdir(f"Cards/{card_bin}")

        # save data as data.json in bin folder
        with open(f"Cards/{card_bin}/data.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        exit()