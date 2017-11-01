import csv

#import xlrd
from pprint import pprint

count = {}
coun = {}
data = {}
#st = {}
d = {}
f= 0
with open('Книга2.csv') as good_file:
    read_file = csv.DictReader(good_file, delimiter = ';')
    for row in read_file:
        for name, p in row.items():
            if name == '':
              count = dict.fromkeys([p],None)
              coun.update(count)
              c = p
            else:
              data = dict.fromkeys([name],p)
              d.update(data)
        st = d.copy()
        coun[c] = st
    print(coun)


