import random

from basic_info import Basic_Info

contact_subsection = {}

class Partner():
    """docstring for Module"""
    def __init__(self, **kwargs):
        self.num_of_contacts = input('Enter the number of contacts: ')
        if int(self.num_of_contacts):
            contact_num = int(self.num_of_contacts)
            while contact_num > 0:
                self.contact = "Contact {}".format(contact_num)
                self.dept = input('[{}] Department: '.format(self.contact))
                self.title = input('[{}] Title: '.format(self.contact))
                self.first_name = input('[{}] First Name: '.format(self.contact))
                self.last_name = input('[{}] Last Name: '.format(self.contact))
                self.phone = input('[{}] Phone Number: '.format(self.contact))
                self.notes = input('[{}] Notes: '.format(self.contact))
                contact_subsection[self.contact] = {'First Name': self.first_name, 'Last Name': self.last_name}
                contact_num -= 1
                print('{}\n'.format(contact_subsection))
        self.address = input('Partner Address: ')

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "\nContacts:{},\nAddress: {}".format(contact_subsection, self.address,)

    