# ppt2note

這是一個利用 openai api 來快速整理 PPT 重點的程式
他能做到：
1. 整理重點
2. 補充相關知識
3. 翻譯


前置：
Windows 需要安裝 PowerPoint
Mac、Linux 需要安裝 libreoffice
~~~Terminal:
brew install libreoffice
~~~

Mac 或者 Linux 請將 tt.py 刪除，改成使用 tt_Mac.py，並將 tt_Mac.py 改名為 tt.py

使用方法：

1. 取得 openai api token 並放到 openai_token.txt
2. pip install requirements.txt
3. 將你要整理的 ppt 改名為 tt.ppt，放到資料夾下
4. python3 main.py
5. 出現 「done」 後，東西就存在 output.txt
