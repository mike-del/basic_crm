import random
import os
import sys


# Memory for partner ids created in init
partner_id = []
# Memory for all partner records
partner_memory = {}

#Function to clear the terminal window
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Partner class: create, print, edit
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

        info = {self.partner_uid :{'department': self.dept, 'title': self.title, 'first name': self.first_name, 'last name': self.last_name, 'phone': self.phone, 'address': self.address, 'notes': [self.notes], }}

        if self.company in partner_memory:
            partner_memory[self.company].append(info)
        else:
            partner_memory[self.company] = info

        # This simply proves that the emplyee information is being saved in the employee_memory dictionary
        # This can be (and probably should be) removed at some point
        print(partner_memory) 

    def __str__(self):
        return "\nID #: {},\nName:{} {},\nPhone Number: {},\nAddress: {},\nDepartment: {},\nTitle: {},\nNotes: {},\n".format(self.partner_uid, self.first_name, self.last_name, self.phone, self.address, self.dept, self.title, self.notes)

    def edit_partner_memory():

        def print_edit_intro():
            print('''
Instructions: Enter the option number that you wish to execute.
Options: [1] Enter the identification number.
         [2] Enter the business name.
         [3] Enter a different record value.
         [4] EXIT edit mode
                ''')
            return int(input('> '))
        
        while True:
            search_by = print_edit_intro()
                
            for company_key, company_value in partner_memory.items():
                    for id_key, id_value in company_value.items():
                        for body_key, body_value in id_value.items():
                            if search_by == 1:
                                clear()
                                print('''
Please enter the identification number of the record that you wish to edit.
                                    ''')
                                search_by_value = input('> ').strip()
                            elif search_by == 2:
                                clear()
                                print('''
Please enter the company name that you wish to edit.
                                    ''')
                                search_by_value = input('> ').strip().lower()
                            elif search_by == 3:
                                clear()
                                print('''
Please enter a record value field.
                                    ''')
                                search_by_value = input('> ').strip().lower()
                            else:
                                clear()
                                return
                            if search_by_value == str(id_key):
                                id_dict = partner_memory[company_key][id_key]
                                clear()
                            elif search_by_value == company_key:
                                id_dict = partner_memory[company_key][id_key]
                                clear()
                            elif search_by_value == body_value:
                                id_dict = partner_memory[company_key][id_key]
                                clear()

                            print('''
Choose an attribute to edit:
[1] Company: {}
[2] First Name: {}
[3] Last Name: {}
[4] Title: {}
[5] Department: {}
[6] Address: {}
[7] Notes: {}
                                '''.format(company_key, id_dict['first name'], id_dict['last name'], id_dict['title'], id_dict['department'], id_dict['address'], id_dict['notes']))
                            att_choice = int(input('> '))
                            if att_choice == 1:
                                new_company_name = input('New Company Name:\n> ')
                                partner_memory[new_company_name] = partner_memory.pop(company_key)
                                return print(partner_memory)
                            elif att_choice == 2:
                                new_first_name = input('New First Name:\n> ')
                                id_dict['first name'] = new_first_name
                                return print(partner_memory)
                            elif att_choice == 3:
                                new_last_name = input('New Last Name:\n> ')
                                id_dict['last name'] = new_last_name
                                return print(partner_memory)
                            elif att_choice == 4:
                                new_title_name = input('New Title Name:\n> ')
                                id_dict['title'] = new_title_name
                                return print(partner_memory)
                            elif att_choice == 5:
                                new_department_name = input('New Department Name:\n> ')
                                id_dict['department'] = new_department_name
                                return print(partner_memory)
                            elif att_choice == 6:
                                new_address_name = input('New Address:\n> ')
                                id_dict['address'] = new_address_name
                                return print(partner_memory)
                            elif att_choice == 7:
                                print('''
[1] Add a new note
[2] Delete all notes.
[3] Delete all notes and add a new note.
                                    ''')
                                note_edit_choice = int(input('> '))
                                if note_edit_choice == 1:
                                    print("Add a new note:")
                                    new_note = input('> ')    
                                    id_dict['notes'].append(new_note)
                                    return print(partner_memory)
                                elif note_edit_choice == 2:
                                    id_dict['notes'] = []
                                    return print(partner_memory)
                                elif note_edit_choice == 3:
                                    print("Delete all notes and add a new note:")
                                    new_note = input('> ')
                                    id_dict['notes'] = [new_note]
                                    return print(partner_memory)
                            else:
                                clear()
                                print('''
That is not a valid record. Please try again.
                                    ''')
