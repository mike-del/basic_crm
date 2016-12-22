import random

from basic_info import Basic_Info

# List to store randomly created employee ids. 
# This ensures that there are no duplicate emplyee ides
employee_id = []
# Dictionary to store all employee records
employee_memory = {}


class Employee(Basic_Info):
    
    """docstring for Module"""
    def __init__(self, basic_info, **kwargs):
        def make_emp_id():
            num = random.randint(1,999)
            if num in employee_id:
                pass
            else:
                employee_id.append(num)
                return num
        self.emp_uid = make_emp_id()
        self.dept = basic_info.dept
        self.title = basic_info.title
        self.first_name = basic_info.first_name
        self.last_name = basic_info.last_name
        self.phone = basic_info.phone
        self.address = basic_info.address
        self.notes = basic_info.notes
        self.social_security_num = int(input('Social security number: '))
        self.hr_pay_rate = int(input('Hourly pay rate: '))

        for key, value in kwargs.items():
            setattr(self, key, value)

        

        employee_memory[self.emp_uid] = {'Department': self.dept, 'Title': self.title, 'First Name': self.first_name, 'Last Name': self.last_name, 'Phone': self.phone, 'Address': self.address, 'Notes': self.notes, 'Pay Rate': self.hr_pay_rate}

        # This simply proves that the emplyee information is being saved in the employee_memory dictionary
        # This can be (and probably should be) removed at some point
        print(employee_memory) 

    def __str__(self):
        return "\nID #: {},\nName:{} {},\nPhone Number: {},\nAddress: {},\nDepartment: {},\nTitle: {},\nHourly Pay Rate: {},\nNotes: {},\n".format(self.emp_uid, self.first_name, self.last_name, self.phone, self.address, self.dept, self.title, self.hr_pay_rate, self.notes)

    # This prints the employee's social security. The purpose is so that the ssn doesn't auto print for security reasons
    def print_ssn(self):
        print(self.social_security_num)

