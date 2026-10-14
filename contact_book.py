import json

contacts  = []

def save_to_file():
    with open("contacts.json","w") as f:
        json.dump(contacts,f)


def load_from_file():
    global contacts
    try:
        with open("contacts.json","r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

load_from_file()

def add_contacts():
    name = input("Name:")
    phone = input("phone:")
    contacts.append({"name":name,"phone": phone})
    save_to_file()
    print("saved!")

def show_all():
    if len(contacts)==0:
        print("No contacts Saved")

    else:
        for c in contacts:
            print(c["name"], "--->",c["phone"]) 


def search():
    query = input("Search Name :")
    found  = False
    for c in contacts:
        if c["name"].lower()==query.lower():
            print("found",c["name"], "--->",c["phone"])
            found  = True
    if not found:
        print("not found")


while True:
    print("\n1. Add  2. Show all  3. Search  4. Quit")
    choice = input("Choose: ")
    if choice == "1":
        add_contacts()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice.")