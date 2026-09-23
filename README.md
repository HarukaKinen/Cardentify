# Cardentify

本仓库是 Cardentify 的 **Issue 收集仓库**，用于接收新卡面、补充卡面资料，以及纠正现有资料。浏览已收录的卡面，请访问 [Cardentify](https://cards.no2.ac/)。

## 卡面来源与获取方式

### 收录范围

本站仅收录由以下服务「按原样」提供的卡面，优先级从高到低依次为：

1. Apple Pay、Google Pay、PayPal
2. Samsung Pay、Mi Pay、云闪付

只接受**横板**卡面。**不接受**来自以上服务以外的任何卡面，如果你觉得其来源质量极高，请在 Issue 中挑战该条规则，我们会考虑添加。

## 提交 Issue 前请阅读

提交新卡面时，请遵循以下要求：

1. **直接在 Issue 中上传卡面文件**，不要只提供网盘链接、临时下载地址或截图。
2. **按获取时的原样提交文件**。请勿裁剪、缩放、压缩、转码、描边、移除背景、添加水印，或进行其他二次处理。如果文件使用特殊扩展名（例如 Mi Pay 的 `.0`），且你不确定如何处理，请直接保留原文件；如果 GitHub 不支持上传该格式，可将原文件打包为 ZIP 后上传。
3. **明确注明卡面来源**，例如 Apple Pay、Google Pay、PayPal、Samsung Pay、Mi Pay 或云闪付。
4. 一个 Issue 可以提交多张卡面；如同时上传多个文件，请尽量说明每个文件对应的卡片。
5. **请勿上传任何敏感信息，尤其是 `pass.json`。** 如果不慎上传或泄露了银行卡资料，请立即联系发卡机构挂失或采取其他必要的安全措施。即使删除或编辑 Issue，相关内容仍可能保留在通知、缓存或历史记录中。

### 建议提供的资料

以下资料并非必填，但请在条件允许的情况下尽可能提供。无法确认的内容可以留空，请勿猜测：

- 银行或发卡机构的当地语言名称、英文名称、所属国家或地区，以及官方网站；
- 卡片的官方名称；可参考 `pass.json` 中的名称，但**请勿上传 `pass.json` 本身，其中可能包含 CVV 等敏感信息**；
- 卡片类型，例如 Credit、Debit 或 Prepaid（**优先以卡面或卡背标注为准**）；
- 卡组织，例如 Visa、Mastercard、American Express、JCB、UnionPay 或 Discover（**优先以卡面或卡背标注为准**）；
- 卡片等级，例如 Platinum、Gold、Signature、Infinite 或 World Elite（**优先以卡面或卡背标注为准**）；
- 卡片的发行国家或地区；
- 卡面来源；
- 卡片可能使用的六位或八位 BIN/IIN。BIN/IIN 仅用于辅助识别，无法确认时可以不提供，且**请勿提交完整卡号**；
- 如果发卡机构与实际资金结算机构不同，请提供资金结算机构的相关资料（**优先以卡面或卡背标注为准**）。

## 透过 Apple Pay 获取卡面

### 如果你拥有配备 Touch ID 的 Mac

请参见美卡论坛的[这篇帖子](https://www.uscardforum.com/t/topic/29408)，你也可以在帖子中找到更多由论坛坛友提供的高清卡面。

### 如果你拥有配备 Touch ID 或 Face ID 的 iPhone 或 iPad

尝试获取 root 权限（比如越狱），进入 `/var/mobile/Library/Passes/Cards/` 目录找到卡面。

> **请注意：** 其中 `pass.json` 存放着关于其卡片的所有隐私信息，包括 CVV；请务必在处理该文件副本时小心谨慎，不要发送给除你之外的任何人。

## 透过 Google Pay 获取卡面

### 如果你拥有支持 Google Pay 非接功能的 Android 设备

获取 root 权限，进入 `/data/data/com.google.android.apps.walletnfcrel/cache/image_manager_disk_cache/` 目录找到卡面。请注意，该目录不会保存没有验证的卡面文件，你需要先在 Google Pay 中完成卡的验证。

## 透过 Mi Pay 获取卡面

### 如果你拥有支持 Mi Pay 非接功能的小米或红米设备

获取 root 权限，进入 `/data/data/com.miui.tsmclient/cache/image_manager_disk_cache/` 目录找到卡面。其中卡面图片文件格式为 `.0`，但可以直接使用图片格式打开。

## 透过云闪付获取卡面

### 如果你拥有已越狱的 iOS 设备

确保已拥有 root 权限，并对云闪付 App 隐藏越狱状态，否则云闪付会拒绝启动。越狱环境下使用支付软件风险较高，请自行承担风险。

打开持卡列表并等待云闪付加载卡面；更多卡面列表中的图片不会自动缓存，需要先选择并保存。随后进入 `/private/var/mobile/Containers/Data/Application/[云闪付 App 的 UUID]/Library/Caches/com.hackemist.SDImageCache/default/` 目录找到卡面。

### 透过中国银联网站

前往[中国银联 [95516.com]](https://mobilepay.95516.com/home/index) 网站，使用云闪付账号登录并进入卡管理，即可查看已经绑定的卡片；你可以通过浏览器审查元素直接访问源文件。
