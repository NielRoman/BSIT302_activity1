Studs = [ "Roman", "May ann"]
list = True
while list:
	print("""
--------------------------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		C. Enter A Student's Name
		R. Show The Students List
		U. Update The Students List
		D. Delete A Students Name
		X. EXIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------------------------
		

		""")

	list = input ("What would you like to do? ")
	if list =="C":
		create = str (input ("Enter the name of the student: "))
		Studs.append(create)
		print ("Added " + create + " to the list")
		print (Studs)

	elif list =="D":
		print (Studs)
		void = int (input ("Enter index number of the student to be remove: "))
		print ("Would you like to delete? " + Studs[void])
		pop = True
		while pop:
			boolean = str (input(" Yes or No?"))
			if boolean == "Yes":
				print ("Successfully deleted " + Studs[void])
				
				print ("These are the name of the students: " + Studs.pop(void))
				print (Studs)
				pop = None
				
			elif boolean == "No":
				print ("No names were deleted: ")
				print (Studs)
				pop = None
			else:
				print ("Invalid Choice")

	elif list == "U":
		print (Studs)
		update = int (input ("Enter index number(0-2+) of the name to update: "))
		print (Studs[update] + " is selected")
		updated = str (input ("What would you like to change it to? "))
		Studs [update] = updated
		print ("Change successful!")
		print (Studs)

	elif list == "R":
		print ("The Students Entered: ")
		print (Studs)

	elif list == "X":
		print ("End Of The Session")
		list = None

	else:
		print ("The User Has Entered An Invalid Selection")