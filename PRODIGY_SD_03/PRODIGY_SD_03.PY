import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave a field blank to keep the current value.")
            name = input(f"Enter new name (current: {contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"Enter new phone (current: {contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"Enter new email (current: {contacts[index]['email']}): ") or contacts[index]['email']
            contacts[index] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit an existing contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
