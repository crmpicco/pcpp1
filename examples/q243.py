import csv

# Writing CSV data
data = [
    {'Name': 'John', 'Age': 30, 'City': 'New York'},
    {'Name': 'Jane', 'Age': 25, 'City': 'Los Angeles'}
]

with open('data_dict.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Reading CSV data
with open('data_dict.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Age'], row['City'])
