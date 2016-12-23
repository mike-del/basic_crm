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
		if module_choice == 'p':
			print('''

Would you like to start a new partner record?
(Enter [Y]es to create a new partner record
or enter [N]o to exit. )

				''')
			new_record = input("> ")
			clear()
			if new_record == 'y':
				print('\nHow many new records would you like to enter?\n')
				num_record = int(input("> "))
				clear()
				while num_record:
					new_partner = Partner()
					num_record -= 1
					clear()
					print(new_partner)
		elif module_choice == 'e':
			new_record = input('Start new record? ')
			clear()
			if new_record == 'y':
				new_emp_id_info = Employee()
				print(new_emp_id_info)
		