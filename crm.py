import datetime
import logging
import os
import sys
import pdb

import basic_info
from basic_info import Basic_Info
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
	print('Pick a module: [P]artner or [E]mployee')
	print('Enter [Q]uit to end this program')
	module_choice = input("> ")
	clear()
	return module_choice

print('Welcome to Intrepid CRM \n\n')
while True:
	module_choice = print_options()
	if module_choice == 'q':
		break
	if module_choice in 'pe':
		if module_choice == 'p':
			new_record = input('Start new record? ')
			if new_record == 'y':
				new_partner = Partner(Basic_Info())
				print(new_partner)
		elif module_choice == 'e':
			new_record = input('Start new record? ')
			if new_record == 'y':
				new_emp_id_info = Employee(Basic_Info())
				print(new_emp_id_info)
		