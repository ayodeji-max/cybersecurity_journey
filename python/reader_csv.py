import csv
with open("contacts.csv","r") as file:
    reader=csv.DictReader(file)
    contacts={}
    for row in reader:
        contacts[row["name"]]= {
        "phone": row["phone"],
        "email": row["email"]
    }
        print(contacts)

