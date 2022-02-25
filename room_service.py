#This is the list of guests in the hotel
guests = {'123':'Zaya', '134':'Michelle', '204':'Jack'}

room = input ("Please enter your room number: ")
name = input ("Please enter your name: ")

if guests[room].lower()==name.lower():
  print ('Correct')
else:
  print ('Incorrect')
