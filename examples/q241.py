import csv

# Writing CSV data
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', 30, 'New York'])
    writer.writerow(['Jane', 25, 'Los Angeles'])

# Reading CSV data
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
