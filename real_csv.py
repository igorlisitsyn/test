import csv

def write_csv(data):
    with open('names.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['surname'], data['age']))

def main():
    d = {'name': 'Petr', 'surname': 'Ivanov', 'age': 20}
    d1 = {'name': 'Oksana', 'surname': 'Petrova', 'age': 18}
    d2 = {'name': 'Detochkin', 'surname': 'Voljanin', 'age': 40}

    l = [d, d1, d2]

    for i in l:
        write_csv(i)




if __name__ == '__main__':
    main()
