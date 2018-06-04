import csv

def write_csv(data):
    with open('names.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['surname'], data['age']))


def write_csv2(data):
    with open('name2.csv', 'a') as f:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)




def main():
    d = {'name': 'Petr', 'surname': 'Ivanov', 'age': 20}
    d1 = {'name': 'Oksana', 'surname': 'Petrova', 'age': 18}
    d2 = {'name': 'Detochkin', 'surname': 'Voljanin', 'age': 40}

    l = [d, d1, d2]

#    for i in l:
#        write_csv(i)
    with open('cmc.csv', 'r') as f:
        fil = ['name', 'sokr', 'url', 'dev']
        reader = csv.DictReader(f, fieldnames=fil)

        for row in reader:
            print(row)



if __name__ == '__main__':
    main()
