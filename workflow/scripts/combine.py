# must be used inside the out directory where the .csv files are located

import os
import csv

dir='.'
files = []
for file in os.listdir(dir):
    if file.endswith('.csv'):
         files.append(file)

with open('combine.csv', 'w', newline='') as fw:
        cw = csv.writer(fw, delimiter='\t')
        for file in files:
            with open(file, newline='') as f:
                for row in csv.reader(f, delimiter='\t'):
                    row.append(file)
                    cw.writerow(row)
