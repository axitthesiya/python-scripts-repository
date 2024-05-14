class PhoneDirectory:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number, **kwargs):
        if not name.strip():
            return "Name cannot be empty."
        if not number.isdigit() or len(number) != 10:
            return "Number must be a 10-digit integer."
        self.contacts[name] = {"number": number, **kwargs}
        return f"Contact added: {name}, Number: {number}"

    def search_contact(self, key):
        if not key.strip():
            return "Please provide a name or number to search."
        for name, contact_info in self.contacts.items():
            if key == name or key == contact_info["number"]:
                return f"Name: {name}, Number: {contact_info['number']}, {', '.join([f'{k}: {v}' for k, v in contact_info.items() if k != 'number'])}"
        return "Contact not found."

    def update_contact(self, identifier, new_number, **kwargs):
        if not identifier.strip():
            return "Identifier (name or number) cannot be empty."
        contact = None
        for name, contact_info in self.contacts.items():
            if identifier == name or identifier == contact_info["number"]:
                contact = name
                break
        if not contact:
            return f"Contact '{identifier}' not found."
        if not new_number.isdigit() or len(new_number) != 10:
            return "New number must be a 10-digit integer."
        self.contacts[contact]["number"] = new_number
        for key, value in kwargs.items():
            self.contacts[contact][key] = value
        return f"Contact updated: {contact}, New Number: {new_number}"

    def delete_contact(self, key):
        if not key.strip():
            return "Please provide a name or number to delete."
        
        keys_to_delete = []
        for name, contact_info in self.contacts.items():
            if key == name or key == contact_info["number"]:
                keys_to_delete.append(name)

        if not keys_to_delete:
            return "Contact not found."

        for name in keys_to_delete:
            del self.contacts[name]

        return f"Contact '{key}' deleted."

    def list_contacts(self):
        if not self.contacts:
            return "No contacts found."
        contact_list = "\n".join([f"Name: {name}, Number: {contact_info['number']}, {', '.join([f'{k}: {v}' for k, v in contact_info.items() if k != 'number'] )}" for name, contact_info in self.contacts.items()])
        return f"Contacts:\n{contact_list}"

if __name__ == "__main__":
    phone_book = PhoneDirectory()
    print("Welcome to your phone directory!")
    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number (10 digits): ")
            while len(number) != 10:
                print("Number must be 10 digits long.")
                number = input("Enter number (10 digits): ")
            additional_info = {}
            while True:
                key = input("Enter additional info key (press Enter to skip): ")
                if not key:
                    break
                value = input(f"Enter value for {key}: ")
                additional_info[key] = value
            print(phone_book.add_contact(name, number, **additional_info))

        elif choice == "2":
            key = input("Enter name or number to search: ")
            print(phone_book.search_contact(key))

        elif choice == "3":
            identifier = input("Enter name or number of contact to update: ")
            new_number = input("Enter new number (10 digits): ")
            while len(new_number) != 10:
                print("Number must be 10 digits long.")
                new_number = input("Enter new number (10 digits): ")
            additional_info = {}
            while True:
                key = input("Enter additional info key to update (press Enter to skip): ")
                if not key:
                    break
                value = input(f"Enter new value for {key}: ")
                additional_info[key] = value
            print(phone_book.update_contact(identifier, new_number, **additional_info))

        elif choice == "4":
            key = input("Enter name or number of contact to delete: ")
            print(phone_book.delete_contact(key))

        elif choice == "5":
            print("Whole list of your contacts.....")
            print(phone_book.list_contacts())

        elif choice == "6":
            print("Excution is Starting.....")
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
