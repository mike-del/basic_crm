import datetime
import logging
import os
import sys
import pdb

import employee
from employee import Employee
import partner
from partner import Partner

logging.basicConfig(filename='newlog.log', level=logging.DEBUG)

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def print_options():
	print('''

Pick a module: [P]artner or [E]mployee
(Enter [Q]uit to end this program )

				''')
	module_choice = input("> ")
	clear()
	return module_choice

clear()
print('Welcome to Intrepid CRM')
while True:
	module_choice = print_options()
	if module_choice == 'q':
		break

	if module_choice in 'pe':
		print('''
Instructions: Enter the option number that you wish to execute.
Options: [1] Create a new record
	 [2] Edit an existing record
	 [3] Quit Partner Module
	 [4] Close and Save Intrepid CRM
			''')
		new_record = int(input("> "))
		clear()
		if new_record == 1:
			print('\nHow many new records would you like to enter?\n')
			num_record = int(input("> "))
			clear()
			while num_record:
				if module_choice == 'p':
					new_partner = Partner()
					num_record -= 1
					print(new_partner)
				elif module_choice == 'e':
					new_employee = Employee()
					num_record -= 1
					print(new_employee)
		elif new_record == 2:
			if module_choice == 'p':
				Partner.edit_partner_memory()
			elif module_choice == 'e':
				Employee.edit_employee_memory()
	