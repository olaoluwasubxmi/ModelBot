#remove every http:// and https:// from the csv file 'agencies.csv'


import csv
import os

#open the csv file
with open('agencies.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

#remove every http:// and https:// from the csv file 'agencies.csv'
for i in range(len(your_list)):
    for j in range(len(your_list[i])):
        your_list[i][j] = your_list[i][j].replace('http://', '')
        your_list[i][j] = your_list[i][j].replace('https://', '')


#remove every row that has no value in the second column
your_list = [x for x in your_list if x[1] != '']

#write the new csv file
with open('agencies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(your_list)
