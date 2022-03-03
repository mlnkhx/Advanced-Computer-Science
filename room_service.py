"""
This program...
By Michelle And Enkhzaya
"""

#This is the list of guests in the hotel
from cgi import print_form
from tkinter import Place


guests = {'102':'Julie', '105':'Renee', '107':'Chloe'}
starters = ['salad','paninni']

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
		print ('Yepp')
		Correct_info = True
	else:
		print ('Nope')
		Correct_info = False

	print ('Please, ')
	print (starters)