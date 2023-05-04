import csv
import os

total = 0
total_count = 0

for filename in os.listdir('dados'):

    with open('dados\\'+filename, 'r') as csv_file:
        csv_reader  = csv.reader(csv_file, delimiter=';')
        
        for i in [1,2,3,4,5,6,7,8,9]:
            next(csv_reader)

        for line in csv_reader:
            if line[7] == '':
                continue
            total += float(line[7].replace(",", "."))
            total_count += 1

    
print(total/total_count)