Employee = []
class employ:
    def __init__(self, name, department, position, rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate

list = True
while list:

            print ("""
            *******************************************************************************************
                        Choose your Option
                        [1] Add New Employee
                        [2] Enter Hourly of Employee
                        [3] Show Employee Information
                        [4] Exit""")

            list = input ("Enter Option: ")
            if list == "1":
                name = str(input ("Enter New Employee Name: "))
                department = str (input ("Enter New Employee Department: "))
                position = str (input ("Enter New Employee Position: "))
                rate = int(input("Enter New Employee Rate : "))
                Employee.append(employ (self.name))
                Employee.append(employ (self.department))
                Employee.append(position)
                Employee.append(rate)

            elif list == "2":
                add5 = int (input ("Enter Employee Number: "))
                first_number = int(input("Enter Employee Hours: "))
                second_number = rate
                final_result = first_number * second_number
                print("Employee Salary for {} hours, with a rate of {} per hour is {} ".format(first_number, second_number, final_result))



            elif list == "3":
                for e in Employee:
                    print("***********************")
                    print(Employee.index(e))


            elif list == "4":
                print ("End of your Session")
            else:
                print("The User has entered an invalid syntax.")
