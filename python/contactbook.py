contacts = {}
def add_contact(name, phone, email):
    contacts[name] ={
        "phone": phone,
        "email": email
    }
    print(f"{name} added successfully!")

def show_contacts():
    if len(contacts) == 0:
        print ("No contacts yet!")
    else:
        for name, details in contacts.items():
            print(f"\nName : {name}")
            print(f"phone: {details['phone']}")
            print(f"email: {details['email']}")
def search_contact(name):
    if name in contacts:
        print(f"\nName: {name}")
        print(f"phone : {contacts[name]['phone']}")
        print(f"email : {contacts[name]['email']}")
    else:
        print(f"{name} not found!")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted!")
    else:
        print(f"{name} not found!")
while True:
    print("\n1. Add contact")
    print("\n2. show all contacts")   
    print("\n3. search contact")
    print("\n4. delete contact")
    print("\n0. quit")

    choice = input("choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        name = input("search name: ")
        search_contact(name)
    elif choice =="4":
        name = input("Delete name: ")
        delete_contact(name)
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("invalid choice!")
        
