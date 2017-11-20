import glob
import os.path


migrations = 'Migrations'

ss =[]
files = glob.glob(os.path.join(migrations, "*.sql"))
for file in files:
	ss.append(file)


def search_f(in_cons):
	ss_2 =[]
	for i in ss:
		with open(i) as ff:
			for f1 in ff:
				dd = f1.find(in_cons)
				print(dd)
			if dd != -1 :

				ss_2.append(i)
	return ss_2

while len(ss):
	print("Количество файлов ->",len(ss))
	print("Поиск ведем ? Да/Нет")
	trig = input()
	if trig =="Нет":
		break
	else:
		print("введите значение поиска")
		in_cons = input()

		print(search_f(in_cons))
		ss = search_f(in_cons)
