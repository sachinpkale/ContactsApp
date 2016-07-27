from src.prefix_tree import PrefixTree

class Contact:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

    def get_name(self):
        name = self.first_name
        if self.last_name:
            name += " " + self.last_name
        return name

class ContactsApp:
    def __init__(self):
        self.first_name_contacts = PrefixTree()
        self.last_name_contacts = PrefixTree()

    def add_contact(self, contact):
        contact = self.__create_contact__(contact)
        if contact:
            self.first_name_contacts.add(contact.get_name().lower(), contact)
            self.last_name_contacts.add(contact.last_name.lower(), contact)

    def search_contact(self, contact):
        contact = contact.strip()
        contacts = []
        contacts += self.first_name_contacts.search(contact.lower())
        last_contacts = self.last_name_contacts.search(contact.lower())
        contacts += [c for c in last_contacts if c not in contacts]
        contacts = [c.get_name() for c in contacts]
        return sorted(contacts, key=len)

    def __create_contact__(self, contact):
        contact = contact.strip()
        if not contact:
            print "Please provide non-empty contact"
            return None
        contact = contact.split(" ", 1)
        first_name = contact[0].strip()
        last_name = ""
        if len(contact) > 1:
            last_name = contact[1].strip()
        contact = Contact(first_name, last_name)
        return contact
