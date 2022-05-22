'''

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]
'''

import csv

portfolio =[]

with open('Data/prices.csv', 'rt') as f:
    rows = csv.reader(f)
    for row in rows: