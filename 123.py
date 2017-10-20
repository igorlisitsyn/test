temperature = []
with open('proba.txt') as tem:
    for line in tem:
        temperature.append(int(line.strip()))

avg = sum(temperature)/len(temperature)
print(avg)

t_average = []
for i in temperature:
    t_average.append(i - avg)

with open('averege_temp', 'w') as t:
    t.write(str(avg))

with open('t_deviation', 'w') as t_d:
    for i in t_average:
        t_d.write("%.2f\n" % i)
