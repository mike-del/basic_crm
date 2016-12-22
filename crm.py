import datetime
import logging
import os
import sys
import pdb

from basic_info import Basic_Info
from employee import Employee
from partner import Partner

logging.basicConfig(filename='newlog.log', level=logging.DEBUG)

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


print('Welcome to Intrepid CRM \n\n')
print('Pick a module: [P]artner or [E]mployee')
print(datetime.datetime.now())
module_choice = input("> ")
clear()
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
		