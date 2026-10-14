# 會議紀錄 skill（meeting-minutes-zh）

這個 skill 讓 Claude 把會議逐字稿整理成正式的繁體中文會議紀錄，用詞照台灣的習慣寫。紀錄固定分成七節，從會議基本資訊寫到後續建議；會中有人提供統計、參考網站或截圖時，會再加第八節「補充資訊」。Claude 整理完會產出 Google 文件或 Word 檔，整理出來的樣子可以看[範例](references/example-minutes.md)。

## 怎麼安裝

把這個網址給你的 AI，請他直接安裝就好：https://github.com/miou1107/meeting-minutes-zh

## 之後怎麼更新

跟你的 AI 說「更新會議紀錄 skill」即可。

## 第一次在新專案使用

先告訴 Claude 這個專案有哪些人、各自負責什麼。Claude 會把這些存成人員對照，之後每一場都會拿來判斷是誰在講話。沒有這份名單，每段話是誰講的都只能靠 Claude 猜。

## 安裝指令（給 AI 或熟悉指令的人看）

- Claude Code 安裝：`git clone https://github.com/miou1107/meeting-minutes-zh ~/.claude/skills/meeting-minutes-zh`
- Claude Code 更新：`git -C ~/.claude/skills/meeting-minutes-zh pull`
- claude.ai 網頁版：下載這個 repo 的 zip 檔，到設定裡的 Skills 頁面上傳。
