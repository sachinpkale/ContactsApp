import unittest
from src.contacts_app import Contact, ContactsApp

class ContactsAppTestCase(unittest.TestCase):

    def test_contact_get_name(self):
    	contact = Contact('Abc', 'Xyz')
        self.assertEquals(contact.get_name(), 'Abc Xyz')

    	contact = Contact('Abc', '')
        self.assertEquals(contact.get_name(), 'Abc')

    	contact = Contact('Abc', 'Xyz')
        self.assertNotEquals(contact.get_name(), 'AbcXyz')

    def test__create_contact__(self):
		contacts_app = ContactsApp()

		self.assertEquals(contacts_app.__create_contact__('Abc').get_name(), 'Abc')
		self.assertEquals(contacts_app.__create_contact__('Abc Xyz').get_name(), 'Abc Xyz')
		self.assertEquals(contacts_app.__create_contact__(' Abc Xyz ').get_name(), 'Abc Xyz')
		self.assertEquals(contacts_app.__create_contact__('Abc  Xyz').get_name(), 'Abc Xyz')
		self.assertEquals(contacts_app.__create_contact__(' Abc   Xyz  ').get_name(), 'Abc Xyz')
		self.assertEquals(contacts_app.__create_contact__('Abc  P  Xyz').get_name(), 'Abc P  Xyz')

if __name__ == '__main__':
    unittest.main()
