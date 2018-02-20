import requests

key = 'trnsl.1.1.20180220T033150Z.c0bc30a93e009632.034c466b5513f3c09c39ab18a7fbc6b4e9d2def4'

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
def translate_proba(my_text):
    params = {
        'key': key,
        'text': my_text,
        'lang': 'ru-fr',
    }
    response = requests.get(url, params=params)
    return response.json()

json_t = translate_proba('петух пошол гулять')
print(''.join(json_t['text']))
