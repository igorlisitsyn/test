from urllib.request import urlopen

from bs4 import BeautifulSoup
import csv

def get_url(url):
    r = urlopen(url)
    bsobj = BeautifulSoup(r, 'lxml')
    return bsobj


def ref(s):
    r = s.split()[0]
    r = r.replace(',', '')
    return r

def write_csv(data):
    with open('plagin.csv', 'a') as f:
        wr = csv.writer(f)
        wr.writerow((data['name'],data['url'],data['reyting']))

def f_url(bsobj):
    popup = bsobj.find_all('section')[1]
    plagins = popup.find_all('article')


    for plagin in plagins:
        n = plagin.find('h2').text
        url = plagin.find('h2').find('a').get('href')
        count = plagin.find('span', class_= 'rating-count').find('a').text
        reyting = ref(count)

        data = {'name': n, 'url': url, 'reyting': reyting}
#        print(data)
        write_csv(data)


#    return plagins


def main():
    url = 'https://wordpress.org/plugins/'
    print(f_url(get_url(url)))


if __name__ == '__main__':
    main()
