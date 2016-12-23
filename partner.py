import random

contact_subsection = {}
partner_id = []
partner_memory = {}


class Partner():
    """docstring for Module"""
    def __init__(self, **kwargs):
        def make_partner_id():
            num = random.randint(1,999)
            if num in partner_id:
                pass
            else:
                partner_id.append(num)
                return num

        self.partner_uid = make_partner_id()
        self.company = input('Company: ')
        self.first_name = input('First name: ')
        self.last_name = input('Last name: ')
        self.phone = input('Phone number: ')
        self.address = input('Address: ')
        self.title = input('Title: ')
        self.dept = input('Department: ')
        self.notes = input('Notes: ')

        for key, value in kwargs.items():
            setattr(self, key, value)

        partner_memory[self.partner_uid] = {'Department': self.dept, 'Title': self.title, 'First Name': self.first_name, 'Last Name': self.last_name, 'Phone': self.phone, 'Address': self.address, 'Notes': self.notes, }

        # This simply proves that the emplyee information is being saved in the employee_memory dictionary
        # This can be (and probably should be) removed at some point
        print(partner_memory) 

    def __str__(self):
        return "\nID #: {},\nName:{} {},\nPhone Number: {},\nAddress: {},\nDepartment: {},\nTitle: {},\nNotes: {},\n".format(self.partner_uid, self.first_name, self.last_name, self.phone, self.address, self.dept, self.title, self.notes)
