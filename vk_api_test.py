from urllib.parse import urlencode, urlparse
import requests

Authoriz_url = 'https://oauth.vk.com/authorize'
Version = '5.60'
App_id = '6397733'

author_data = {
    'client_id': App_id,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends, status',
    'v': Version,
}
print('?'.join((Authoriz_url, urlencode(author_data))))

token_url = 'https://oauth.vk.com/blank.html#access_token=2618513dfc5e22199d33f63d2c90f4f40e79b0540878010c153a95092b5ec8825032b9bd7383b311c6e73&expires_in=86400&user_id=476807711'
o = urlparse(token_url)
frag = dict((i.split('=') for i in o.fragment.split('&')))
access_token = frag['access_token']

params = {
    'access_token': access_token,
    'v': Version
}

response = requests.get('http://api.vk.com/method/friends.getOnline', params)

print(response)
#for user_id in response.json()['response']:
#    response = requests.get('http://api.vk.com/method/users.get', {'user_id': user_id})
#    print(response.json())

#print(frag)
