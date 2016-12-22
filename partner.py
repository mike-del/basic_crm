import random

from basic_info import Basic_Info

contact_subsection = {}
partner_id = []
partner_memory = {}


class Partner(Basic_Info):
    
    """docstring for Module"""
    def __init__(self, basic_info, **kwargs):
        def make_partner_id():
            num = random.randint(1,999)
            if num in partner_id:
                pass
            else:
                partner_id.append(num)
                return num
        self.partner_uid = make_partner_id()
        self.dept = basic_info.dept
        self.title = basic_info.title
        self.first_name = basic_info.first_name
        self.last_name = basic_info.last_name
        self.phone = basic_info.phone
        self.address = basic_info.address
        self.notes = basic_info.notes
        # contact_subsection[self.contact] = {'First Name': self.first_name, 'Last Name': self.last_name}
        # contact_num -= 1
        # print('{}\n'.format(contact_subsection))

        for key, value in kwargs.items():
            setattr(self, key, value)

        

        partner_memory[self.partner_uid] = {'Department': self.dept, 'Title': self.title, 'First Name': self.first_name, 'Last Name': self.last_name, 'Phone': self.phone, 'Address': self.address, 'Notes': self.notes, }

        # This simply proves that the emplyee information is being saved in the employee_memory dictionary
        # This can be (and probably should be) removed at some point
        print(partner_memory) 

    def __str__(self):
        return "\nID #: {},\nName:{} {},\nPhone Number: {},\nAddress: {},\nDepartment: {},\nTitle: {},\nNotes: {},\n".format(self.partner_uid, self.first_name, self.last_name, self.phone, self.address, self.dept, self.title, self.notes)
