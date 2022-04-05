from datetime import datetime,date
#Create Class Person
class Person:
    #Class attribute
    organization = "ASU"
    #instant attributes (for each object)
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def age(self):
        #Get today's date object
        today = date.today()
        #Convert DOB from string to a datetime oject
        birthdate = datetime.strptime(self.dob, '%Y/%m/%d')
        #Take into account leap years
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
        #Calculate the age
        year_difference = today.year - birthdate.year
        age = year_difference - one_or_zero
        return age

    def __repr__(self):
        return f"Name: {self.name}, Date of birth: {self.dob}, Age: {self.age()}"

#Create the Student (child class)
class Student(Person):
    def __init__(self, name, dob, grade, subjects):
        super().__init__(name, dob)
        self.grade = grade
        self.subjects = subjects

    def __repr__(self):
        return super().__repr__() + f", Grades: {self.grade}, Subjects: {self.subjects}"

#List of Students
students = []

#Main program
print("Welcome to ASU Student Services")
print("Please enter the information of the student")
print("_______________________________")

while True:
    name = input("Name:")
    while True:
        try:
            dob = input("Date of Birth (yyyy/mm/dd):")
            testdate = datetime.strptime(dob, '%Y/%m/%d')
            break
        except Exception as e:
            print (e)
    grade = input("Grade:")
    subjects = input("Subjects:")

    students.append(Student(name, dob, grade, subjects))

    answer = None
    while answer not in ('y','n'):
        answer = (input("Would you like to enter another student (y/n)")).lower()
    if answer=='n':
        #Print students
        print("You have entered the following students")
        print("________________________________________")
        for students in students:
            print (students)
        break
