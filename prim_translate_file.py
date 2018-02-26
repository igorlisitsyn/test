import requests

key = 'trnsl.1.1.20180220T033150Z.c0bc30a93e009632.034c466b5513f3c09c39ab18a7fbc6b4e9d2def4'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate(text_translate):
    params = {
        'key': key,
        'text': text_translate,
        'lang': 'ru-en',
    }
    response = requests.get(url, params=params)
    return response.json()
tr = ''
with open('sourse.txt', 'r') as text:
    for t in text:
        tr_text = translate(t)
        tr += ''.join(tr_text['text'])+'\n'



with open('sourse_tr.txt', 'w') as t:
    for i in tr:
        t.write(i)

print(tr)
