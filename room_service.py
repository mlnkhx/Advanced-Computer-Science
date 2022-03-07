"""
This program...
By Michelle And Enkhzaya
"""

#This is the list of guests in the hotel
from cgi import print_form
from tkinter import Place


guests = {'102':'Julie', '105':'Renee', '107':'Chloe'}
starters = ['salad','paninni']
main = ['chiken porridge', 'kotlet', 'sushi']
desert = ['ice cream', 'panna cotta',]
Correct_info = False
room = None
name = None

while not Correct_info:
	room = input ("Please enter room number: ")
	if room in guests.keys():
		Correct_info = True
	else:
		Correct_info = False

	name = input ("Please enter your name: ")

	if Correct_info and guests[room].lower()==name.lower():
		print ('Thank you for the information')
		Correct_info = True
	else:
		print ('Please, try again')
		Correct_info = False

print ('Please, choose a starter: ')
print (starters)
print ('please, choose a main: ')
print (main)
print ('please choose desert: ')
print (desert)