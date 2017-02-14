from src.prefix_tree import PrefixTree

"""Contact class provides abstraction of the contact"""
class Contact:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

    def get_name(self):
        """Get full name of a contact by combining first name and last name."""
        name = self.first_name
        if self.last_name:
            name += " " + self.last_name
        return name

"""ContactsApp class provides abstraction of the Application.
   It uses two prefix trees. One for first name and another for last name.
"""
class ContactsApp:
    def __init__(self):
        self.contacts = PrefixTree()

    def add_contact(self, contact):
        """Add contact to both the prefix trees

        :param contact: contact name to be added
        """
        contact = self.__create_contact__(contact)
        if contact:
            self.contacts.add(contact.get_name().lower(), contact)
            self.contacts.add(contact.last_name.lower(), contact)

    def search_contact(self, contact):
        """Search contact from both the prefix trees. Duplicates will be removed.

        :param contact: contact name to be searched
        :return list of contacts matching prefix
        """
        contact = contact.strip()
        contacts = []
        contacts = self.contacts.search(contact.lower())
        contacts = set(contacts)
        contacts = [c.get_name() for c in contacts]
        return sorted(contacts, key=len)

    def __create_contact__(self, contact):
        """Returns a Contact object given a contact name

        :param contact: contact name string
        :return Contact object after cleaning up input string
        """
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
