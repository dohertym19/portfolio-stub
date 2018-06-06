import csv
with open('csvs/basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]

first_names = [row[2] for row in names]
first_names.reverse()


new_row = [2,'wayne','graham','meh']
names.append(new_row)


a_row = [3,'fox','eliza','SO COOL']
names.append(a_row)

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20])

with open('csvs/practice.csv', 'r') as fin:
    our_reader = csv.reader(fin)
    data = [row for row in our_reader]

data[3][3] = 'Ethan'
data[4][2] = 'Brandon'
data[2][4] = 'Tony the cat'

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for row in data:
        csvwriter.writerow(row)


groceries = []
with open('csvs/shopping.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        groceries.append(row)

print(groceries)
