import glob
import os.path

migrations = 'Migrations'

files = glob.glob(os.path.join(migrations, "*.sql"))
for file in files:
	print(file)
