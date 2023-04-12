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
            {"role": "system", "content": f"你是一名資訊工程系的教授，你將會根據接下來輸入的教材，逐行仔細閱讀，使用繁體中文將這份教材整理出重點與補充，讓學生能夠快速閱讀準備考試"}, # 設定角色
            {"role": "user", "content": text} #輸入問題
        ])
response = response['choices'][0]['message']['content']

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(response)

print("done")