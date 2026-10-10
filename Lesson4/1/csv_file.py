import csv
from os import write

with open("user_csv.csv","w",encoding="utf-8",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name","Email","Role"])
    writer.writerow(["Ivan", "Email2@gmil.com", "QA"])
    writer.writerow(["Anna", "Email32@gmil.com", "dev"])


with open("user_csv.csv") as file:
    reader = csv.reader(file)
    print(type(reader))

    for row in reader:
        print(row)

# email= row[1]
# print(email)

with open("user_csv.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["Name"],"-",row["Role"])