import random
import os
import sys

# List to store randomly created employee ids. 
# This ensures that there are no duplicate emplyee ides
employee_id = []
# Dictionary to store all employee records
employee_memory = {}


#Function to clear the terminal window
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Employee():
    
    """docstring for Module"""
    def __init__(self, **kwargs):
        def make_emp_id():
            num = random.randint(1,999)
            if num in employee_id:
                pass
            else:
                employee_id.append(num)
                return num
        self.emp_uid = make_emp_id()
        self.first_name = input('First name: ')
        self.last_name = input('Last name: ')
        self.phone = input('Phone number: ')
        self.address = input('Address: ')
        self.title = input('Title: ')
        self.dept = input('Department: ')
        self.notes = input('Notes: ')
        self.social_security_num = int(input('Social security number: '))
        self.hr_pay_rate = int(input('Hourly pay rate: '))

        for key, value in kwargs.items():
            setattr(self, key, value)

        

        employee_memory[self.emp_uid] = {'department': self.dept, 'title': self.title, 'first name': self.first_name, 'last name': self.last_name, 'phone': self.phone, 'address': self.address, 'notes': [self.notes], 'pay rate': self.hr_pay_rate}

        # This simply proves that the emplyee information is being saved in the employee_memory dictionary
        # This can be (and probably should be) removed at some point
        print(employee_memory) 

    def __str__(self):
        return "\nID #: {},\nName:{} {},\nPhone Number: {},\nAddress: {},\nDepartment: {},\nTitle: {},\nHourly Pay Rate: {},\nNotes: {},\n".format(self.emp_uid, self.first_name, self.last_name, self.phone, self.address, self.dept, self.title, self.hr_pay_rate, self.notes)

    # This prints the employee's social security. The purpose is so that the ssn doesn't auto print for security reasons
    def print_ssn(self):
        print(self.social_security_num)

    def edit_employee_memory():

        def print_edit_intro():
            print('''
Instructions: Enter the option number that you wish to execute.
Options: [1] Enter the identification number.
         [2] Enter a different record value.
         [3] EXIT edit mode
                ''')
            return int(input('> '))
        
        while True:
            search_by = int(print_edit_intro())
            if search_by == 1 or search_by == 2:
                clear()
                print('''
Please enter the information now.
                    ''')
                search_by_value = input('> ').strip()

                for employee_id_key, employee_body in employee_memory.items():

                    for employee_key, employee_value in employee_body.items():
                        
                        if search_by_value == str(employee_id_key) or search_by_value == employee_value:
                            id_dict = employee_memory[employee_id_key]
                            clear()
                            print('''
Choose an attribute to edit:
[1] First Name: {}
[2] Last Name: {}
[3] Department: {}
[4] Title: {}
[5] Pay Rate: {}
[6] Phone: {}
[7] Address: {}
[8] Notes: {}
                                '''.format(id_dict['first name'], id_dict['last name'], id_dict['department'], id_dict['title'], id_dict['pay rate'], id_dict['phone'], id_dict['address'], ", ".join(id_dict['notes'])))
                            att_choice = int(input('> '))
                            if att_choice == 1:
                                new_first_name = input('New First Name:\n> ')
                                id_dict['first name'] = new_first_name
                                return print(employee_memory)
                            elif att_choice == 2:
                                new_last_name = input('New Last Name:\n> ')
                                id_dict['last name'] = new_last_name
                                return print(employee_memory)
                            elif att_choice == 3:
                                new_department_name = input('New Department Name:\n> ')
                                id_dict['department'] = new_department_name
                                return print(employee_memory)
                            elif att_choice == 4:
                                new_title_name = input('New Title Name:\n> ')
                                id_dict['title'] = new_title_name
                                return print(employee_memory)
                            elif att_choice == 5:
                                new_pay_rate = input('New Pay Rate:\n> ')
                                id_dict['pay rate'] = new_pay_rate
                                return print(employee_memory)
                            elif att_choice == 6:
                                new_phone_num = input('New Pay Rate:\n> ')
                                id_dict['phone'] = new_phone_num
                                return print(employee_memory)
                            elif att_choice == 7:
                                new_address_name = input('New Address:\n> ')
                                id_dict['address'] = new_address_name
                                return print(employee_memory)
                            elif att_choice == 8:
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
                                    return print(employee_memory)
                                elif note_edit_choice == 2:
                                    id_dict['notes'] = []
                                    return print(employee_memory)
                                elif note_edit_choice == 3:
                                    print("Delete all notes and add a new note:")
                                    new_note = input('> ')
                                    id_dict['notes'] = [new_note]
                                    return print(employee_memory)
                        else:
                            clear()
                            print('''
That is not a valid record. Please try again.
                                ''')

