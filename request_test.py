import requests

url = 'https://requestb.in/v8jvxiv8'
json = {
    'month': 'May',
    'result': '1:0',
    'komand': 'Yamayka',
}

response = requests.post(url, params= json)
print(response.status_code)

url_2 = 'http://httpbin.org/'
params = {
    id: [1,2,3]
}
response = requests.get(url_2, params = params)
print(response.json())
