# Cardentify 卡面库

该 Repo 仅用于保存并同步卡面数据，网页前端请前往 [Cardentify-Frontend](https://github.com/HarukaKinen/Cardentify-frontend)

## 文件结构

所有数据文件均存放在 `Cards` 文件夹中，`main.py` 负责让 [Github Actions](https://github.com/HarukaKinen/Cardentify/actions) 处理并生成前端所需要的数据并 Force Push 到 `data` 分支。

`Cards` 文件夹中，按照银行常用英文全称命名，`data.json` 为该银行及收录卡面的数据，`[Card_*].png` 为该银行的卡图，图片应当按照 Apple Pay 的 `pass.json` 中卡片名称或其他官方名称命名，且与 `data.json` 中的 `description` 字段一致。

`Cards` 文件夹结构：

```
/Cardentify/
├── Cards/
│   ├── [Bank Name]/
│   │   ├── data.json
│   │   ├── [Card_1].png
│   │   └── [Card_2].png
│   └── ...
├── main.py
└── README.md
```

`data.json` 结构：

```json
{
    "bank": {
        "native_name": "Bank Native Name", // 银行当地语言名称
        "english_name": "Bank English Name", // 银行英文名称
        "country": "US", // 银行所属国家
        "url": "https://www.exmaple.com" // 银行官网链接
    },
    "cards": [
        {
            "description": "Random Debit Card", // "pass.json" 中的卡名称
            "bin": [
                400000 // 卡潜在 BIN 头（六位）
            ],
            "manager": { // 如果该卡发卡行与结算行不同，可以使用该字段指定其资金结算行
                "native_name": "Bank Native Name",
                "english_name": "Bank English Name",
                "country": "US",
                "url": "https://www.exmaple.com"
            },
            "card": {
                "type": "Credit", // 卡类型
                "brand": "VISA", // 发行品牌
                "country": "US", // 发行国家
                "level": "Platinum" // 卡等
            },
            "source": "Apple Pay", // 图片来源
            "ext": "png", // 图片格式，如果需要的图片文件名与 description 字段相同，在此处填写其图片后缀即可，否则忽略该字段，填写下方的 filename 字段
            "filename": "Random Debit Card File Name.png" // 引用的图片文件名，包含其后缀。此字段和 ext 字段只能保留一个
        },
        {
            ...
        }
    ]
}
```

如果对应字段无需填写或无法提供，请删除其对应字段。

## 贡献

如果你不会自行处理 `data.json` 或懒得处理，请携卡图文件和必要的信息提交 Issue，除卡图外请尽可能的提供 `data.json` 中对应的其他信息。

如果你完全看懂了文件结构，欢迎 Pull Request。

### 如何定义资金结算行

美国的大部分虚拟银行借记卡的发行商都不是严格意义上的银行，他们需要委托其他持牌银行进行发卡和资金结算。比如 Apple Cash 由 Green Dot Bank 代结算、Chime 借记卡由 The Bancorp Bank 或 Stride Bank 代结算，但在平时用卡的过程中看不到后者的身影。这种情况下，发卡行为前者（即使他们不是银行），结算行为后者。你可以在其条款内确认，而这些信息通常也会在其网站底部特别标注。如果你有实体卡，卡背面通常也会有相应标注。

还有一种特殊情况，花旗台湾的信用卡业务被星展台湾接管，花旗的卡虽然从各方面看都只有花旗字样，但实际上资金结算已交由星展台湾。在这种情况下，也需要特别指定其资金结算行。

通常情况下，申请卡片的地方为发卡行，而实际提供资金结算的银行为结算行。如果你不确定如何区分，可以在 Issue 中提出。

## Disclaimer

This is a community project. Anyone involved in the project is not associated with any of the banks or companies and no one is employee of them.

Any data in this project is source from publicly available information from the bank and does not involve any confidential documents.
