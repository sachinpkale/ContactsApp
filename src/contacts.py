"""ContactsApp supports two functions:
1. add_contact
2. search_contact

Assumptions:
1. Only prefix based search is supported.
2. As data is being stored in in-memory data structure, it will not be available in subsequent runs of the application.
"""
from src.contacts_app import ContactsApp

if __name__ == "__main__":
    contacts_app = ContactsApp()
    while(True):
        choice = int(input("1) Add contact 2) Search 3) Exit\n"))
        if choice in [1, 2]:
            contact = str(raw_input("Enter name: "))
            if choice == 1:
                contacts_app.add_contact(contact)
            else:
                contacts = contacts_app.search_contact(contact)
                if contacts:
                    for c in contacts:
                        print c
        elif choice == 3:
            print "Happy Searching"
            break
        else:
            print "Please enter 1, 2 or 3"