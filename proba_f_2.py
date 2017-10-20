cites = {}

with open('stat') as l_stroka:
       for line in l_stroka:
           t = l_stroka.readline()
           if len(t.split()) != 0:
                cites[line.strip()] = t.split()


for city, temperatura in cites.items():
    avg = 0
    for tt in temperatura:
        avg += int(tt)
    avg = avg/len(temperatura)
    print(city, avg)

