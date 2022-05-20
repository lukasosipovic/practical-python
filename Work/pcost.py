# pcost.py
#
# Exercise 1.27

import csv
sum = 0
f = open('Data/portfolio.csv')
rows = csv.reader(f)

headers = next(rows)

for line in rows:
    sum = sum + (int(line[1]) * float(line[2]))
print(sum)
