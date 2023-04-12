import pdfplumber
import openai
from tt import ppttopdf

with open('openai_token.txt', 'r') as f:
    openai.api_key = f.read()

ppttopdf()

pdf = pdfplumber.open('tt.pdf')
text = ''
for page in pdf.pages:            
    text += page.extract_text()

response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": f"你是一名資訊工程系的教授，你將會根據接下來輸入的教材產生一份能夠讓學生快速閱讀準備考試的繁體中文筆記，有需要產出圖片就產出文字圖片"}, # 設定角色
            {"role": "user", "content": text} #輸入問題
        ])
response = response['choices'][0]['message']['content']

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(response)

print("done")