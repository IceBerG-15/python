import csv

with open('machine learning\\dataset.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

