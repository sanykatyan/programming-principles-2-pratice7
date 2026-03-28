from connect import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()


def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added.")


def search():
    name = input("Search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%' + name + '%',)
    )

    rows = cur.fetchall()

    if not rows:
        print("Nothing found")
    else:
        for row in rows:
            print(row)


def update():
    name = input("Name to update: ")
    new_phone = input("New phone: ")

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )
    conn.commit()
    print("Updated.")


def delete():
    name = input("Name to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )
    conn.commit()
    print("Deleted.")


def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def menu():
    while True:
        print("\n1.Insert")
        print("2.Search")
        print("3.Update")
        print("4.Delete")
        print("5.Show all")
        print("6.Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            search()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            show_all()
        elif choice == "6":
            break


menu()