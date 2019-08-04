Employee = []
class employ:
	def __init__(self, name, department, position, rate):
		self.name = name
		self.department = department
		self.position = position
		self.rate = rate

list = True
while list:

		print("""
************************************
Choose Your Option:
	[1] Add New Employee's Name
	[2] Enter Hourly Rate Of New Employee
	[3] Show Employee's Information
	[4] Exit
	""")

		list = input ("Enter An Option: ")
		if list == "1":
			name = str(input("Enter New Employee's Name: "))
			department = str(input("Enter New Employee's Department: "))
			position = str(input("Enter New Employee's Position: "))
			rate = int(input("Enter New Employee's Rate: "))
			Employee.append(name)
			Employee.append(department)
			Employee.append(position)
			Employee.append(rate)
			print("The given information are saved!")

		elif list == "2":
			num1 = int(input("Enter Employee's Number: "))
			hour = int(input("Enter Employee's Hours: "))
			num2 = rate
			finResult = hour * num2
			print("The employee's salary for {} hours, with a rate of ${} per hour, will be ${}".format(hour, num2, finResult))
			print("The given information are saved!")

		elif list == "3":
			print ("""************************************
	Employee's Number: {}
	Employee's Name: {}
	Employee's Department: {}
	Employee's Position: {}
	Employee's Hourly Rate: {}
	Employee's Working Hours: {}""".format(num1, name, department, position, rate, hour))



		elif list == "4":
			print("End Of Your Session.")
		else:
			print("The user has entered an invalid syntax.")