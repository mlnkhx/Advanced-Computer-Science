"""
Room Service
By: Michelle And Enkhzaya
"""

#This is the list of guests in the hotel
from cgi import print_form
from tkinter import Place

guests = {'102':'Julie', '105':'Renee', '107':'Chloe'}

starters = ['salad','paninni','vegan terrine']
main = ['chiken porridge', 'kotlet', 'sushi']
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

<<<<<<< HEAD
print ('Please, choose a starter: ')
print (starters)
print ('are you sure of what you ordered? Yes or No? ')
print ('please, choose a main: ')
print (main)
print ('please choose desert: ')
print (desert)
print ('Here are the bills', starters + main + desert )

>>>>>>> d9bd408799c644ef74ac390a0e3260d2fd78d76c
