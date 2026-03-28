phonebook = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    phonebook.append({
        "name": name,
        "phone": phone
    })
  

def show_contacts():
    for contact in phonebook:
        print(contact)


def search():
    query = input("Search name: ")

    for contact in phonebook:
        if query.lower() in contact["name"].lower():
            print(contact)


def delete():
    phone = input("Phone to delete: ")

    for contact in phonebook:
        if contact["phone"] == phone:
          phonebook.remove(contact)
          print("Deleted")
          return
        

def update():
  phone = input("Phone of contact: ")
  new_name = input("New name: ")

  for contact in phonebook:
      if contact["phone"] == phone:
          contact["name"] = new_name
          print("Updated")
          return
      

def menu():
      while True:
        print("1.Add")
        print("2.Show")
        print("3.Search")
        print("4.Update")
        print("5.Delete")
        print("6.Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            break

menu()
