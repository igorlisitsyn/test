from urllib.request import urlopen

from bs4 import BeautifulSoup
import csv

def get_url(url):
    read = urlopen(url)
    bsobj = BeautifulSoup(read, 'lxml')
    return bsobj

def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['name'], data['simvol'], data['url'], data['price']])



def get_page_data(html):
    trs = html.find('table', id = 'currencies').find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_ ='currency-name-container' ).text
        simvol = tds[1].find('a').text
        url = tds[1].find('a').get('href')
        price = tds[3].find('a').get('data-usd')

        data = {'name': name, 'simvol': simvol, 'url': url, 'price': price}
        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_url(url))




if __name__ == '__main__':
    main()
