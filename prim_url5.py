from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re



def url_open(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html, 'lxml')
    return bsobj

def write_csv(date):
    with open('coin.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((date['name'], date['url'], date['price'], date['dev']))


def get_data(obj):
    tab = obj.find('table', id = 'currencies').find('tbody').find_all('tr')
    for tr in tab:
        td = tr.find_all('td')
        name = td[1].find('a', class_ = 'currency-name-container link-secondary night-mode-bold').text.strip()
        ul = 'https://coinmarketcap.com/' + td[1].find('a', class_ = 'currency-name-container link-secondary night-mode-bold').get('href')
        coint = td[3].find('a', class_ = 'price').text.strip()
        dev = td[6].get('data-sort').strip()

        date = {'name': name,
             'url': ul,
             'price': coint,
             'dev': dev}
        write_csv(date)




def main():
    url = 'https://coinmarketcap.com/'
#    get_data(url_open(url))

    while True:
        get_data(url_open(url))

        sou = url_open(url)

        try:
            pattern = 'Next'
            url = 'https://coinmarketcap.com/' + sou.find('ul', class_ = 'pagination bottom-paginator').find('a', text = re.compile(pattern)).get('href')
        except:
            break







if __name__ == '__main__':
    main()
