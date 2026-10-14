# 會議紀錄 skill（vin-meeting-minutes-zh）

這個會議記錄 skill 是由某位不具名的會議達人精心特調過，特別適合台灣一般中小企業，無論用在內部會議、跨單位/跨公司會議都適合。讓 AI 把會議逐字稿整理成正式的繁體中文會議紀錄，用詞照台灣的習慣寫。Claude 整理完會產出 Google 文件或 Word 檔。
只要你手上有逐字稿，即使內容零碎、錯字連連，同樣都能整理出有條有理的會議記錄，且還原的程度非常高。

完成的會議紀錄，可參考 [範例](references/example-minutes.md)。

## 這個 skill 有什麼特色

- **錯字再多、沒標講者的逐字稿也能整理**：Claude 會先讀專案的提案、前幾次的紀錄和人員名單，再修正語音辨識的錯字，判斷每段話是誰講的。
- **沒把握的地方不硬猜**：分不出是誰講的就先寫單位，聽不清楚的字和數字照原文保留，交件時一起列出來請你確認。
- **越用越準**：你更正過的錯字和講者會存進專案的對照表，下一場會議就不會再錯。
- **對內、對外分開寫**：公司內部會議直接寫人名；有客戶或廠商參加的會議只寫單位，客戶離線後的內部討論會刪除。
- **台灣用語、正式語氣**：政府案用公文體，公司內部和企業客戶用正式商務語氣，不寫中國大陸用語，也不寫 AI 常用的套話。
- **格式邏輯一致**：所有專案都用同一套章節，不同場次的紀錄可以直接對照。
- **直接產出 Google 文件**：電腦設定好 Google 登入時，Claude 會建好 Google 文件，並開放給公司同仁加註。之後改版網址不變；有人在文件上改過或留言，Claude 會先停下來問你。

## 紀錄分成哪幾節

| 章節 | 寫什麼 |
|---|---|
| 一、會議基本資訊 | 主題、日期時間、地點、主持人、與會人員、會議資料連結 |
| 二、會議目的 | 這場會議承接什麼、要確認什麼 |
| 三、討論摘要 | 依主題整理，每一條寫清楚是誰的說法 |
| 四、初步共識 | 會中已經同意的事 |
| 五、待確認事項 | 還沒定案的事，以及要向誰確認 |
| 六、行動方案 | 誰負責做什麼、什麼時候完成 |
| 七、其他建議 | 下次會議可以聚焦的事、可以延後的議題 |
| 八、補充資訊 | 會後提供的統計、參考網站、截圖；有額外補充資料才會有此段 |

## 怎麼安裝

把這個網址給你的 AI，請他直接安裝就好：https://github.com/miou1107/vin-meeting-minutes-zh

## 之後怎麼更新

跟你的 AI 說「更新會議紀錄 skill」即可。

## 第一次在新專案使用

先告訴 Claude 這個專案有哪些人、各自負責什麼。Claude 會把這些存成人員對照，之後每一場都會拿來判斷是誰在講話。沒有這份名單，很多段落 Claude 分不出是誰講的，只能先寫單位，再請你逐段確認。

## 安裝指令（給 AI 的指令）

- Claude Code 安裝：`git clone https://github.com/miou1107/vin-meeting-minutes-zh ~/.claude/skills/vin-meeting-minutes-zh`
- Claude Code 更新：`git -C ~/.claude/skills/vin-meeting-minutes-zh pull`
- 如果之前裝的是舊名稱 meeting-minutes-zh，先把資料夾改成新名稱再更新：`mv ~/.claude/skills/meeting-minutes-zh ~/.claude/skills/vin-meeting-minutes-zh && git -C ~/.claude/skills/vin-meeting-minutes-zh remote set-url origin https://github.com/miou1107/vin-meeting-minutes-zh && git -C ~/.claude/skills/vin-meeting-minutes-zh pull`
- claude.ai 網頁版：下載這個 repo 的 zip 檔，到設定裡的 Skills 頁面上傳。
