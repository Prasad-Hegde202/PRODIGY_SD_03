import json


def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts available.")

# Function to edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        choice = int(input("\nEnter the contact number to edit: "))
        if 1 <= choice <= len(contacts):
            contact = contacts[choice - 1]
            print(f"Editing Contact: {contact['name']}")
            contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
            contact['phone'] = input("Enter new phone (leave blank to keep current): ") or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        choice = int(input("\nEnter the contact number to delete: "))
        if 1 <= choice <= len(contacts):
            contacts.pop(choice - 1)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop
def contact_management_system():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_management_system()
