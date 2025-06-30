print("Contact Book")
contacts = {}

def create_contact():
    name = input("Enter the name: ")
    if name in contacts:
        print(f"Contact '{name}' already exists.")
    else:
        phone_number = input("Enter the phone number: ")
        contacts[name] = {'phone_number': phone_number}
        print(f"Contact '{name}' has been created successfully.")

def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' has been deleted successfully.")
    else:
        print("Contact does not exist.")

def update_contact():
    name = input("Enter name to update contact: ")
    if name in contacts:
        phone_number = input("Enter updated phone number: ")
        contacts[name]['phone_number'] = phone_number
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact does not exist.")

def view_contact():
    name = input("Enter the name to view: ")
    if name in contacts:
        print(f"Name: {name}, Phone Number: {contacts[name]['phone_number']}")
    else:
        print("Contact does not exist.")

def view_all_contacts():
    if contacts:
        print("All Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone Number: {info['phone_number']}")
    else:
        print("No contacts found.")

while True:
    print("\nContact Book Menu")
    print("1. Create Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. View Contact")
    print("5. View All Contacts")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        view_contact()
    elif choice == '5':
        view_all_contacts()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")