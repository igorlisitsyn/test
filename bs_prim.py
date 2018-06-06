from bs4 import BeautifulSoup
import re

def get_ssal(s):
    patt = r'\d{1,9}'
    sal = re.findall(patt, s)
    print(sal)

def main():
    f = open('index.html').read()
    soup = BeautifulSoup(f, 'lxml')
    salary = soup.find_all('div', {'data-set': 'salary'})
    for i in salary:
        get_ssal(i.text)
  #
#   print(al)



if __name__ == '__main__':
    main()
