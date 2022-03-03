#This is the list of guests in the hotel
room = input (“Please enter room number: “)
if room in guests.keys():
	Correct_info = True
else:
	Correct_info = False

name = input (“Please enter your name:”)’

if correct_info and guests[room].lower()==name.lower():
	correct_info = True
else:
	correct_info = flase
