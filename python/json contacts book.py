import json
import os

FILENAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILENAME):
        f = open(FILENAME, "r")
        contacts = json.load(f)
        f.close()
        return contacts
    else:
        return{}

def save_contacts(contacts):
    f = open(FILENAME, "w")
    json.dump(contacts, f)
    f.close()
contacts = load_contacts()

def add_contact(name, phone, email):
    contacts[name] ={
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print(f" {name} added successfully!")
def show_contacts():
    if len(contacts) ==0:
        print ("no contacts yet!")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"\nphone: {details['phone']}")
            print(f"\nemail: {details['email']}")


def search_contact(name):
    if name in contacts:
        print(f"\nName: {name}")
        print(f"\nphone: {contacts['phone']}")
        print(f"\nemail: {contacts['eamil']}")
    else:
        print(f"{name} not found!")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    else:
        print(f"{name} not found")



while True:
    print("\n1. Add contacts")
    print("\n2. show all  contacts")
    print("\n3. search contacts")
    print("\n4. delete contacts")
    print("0. Quit")

    choice = input("choose: ")

    if choice == "1":
        name= input("Name: ")
        phone = input("Phone: ")
        email =input("Email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        name = input("search name: ")
        search_contact(name)
    elif choice == "4":
        name = input("delete name: ")
        delete_contact(name)
    elif choice == "0":
        print("goodbye!")
        break
    else:
        print("invalid choice!")
