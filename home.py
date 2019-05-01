from company import Employee,Supervisor
print("welcome to company")
while True:
	print("\n \n what would you like to see:\n1.salary\n2.disp_details\n3.check\n4.calc_tax\n5.Exit")
	choice=int(input("enter your choice: "))
	print(choice)
	sup_id=[12,13,14,15,16,17]
	emp_name=raw_input("enter the name: ")
	emp_id=int(input("enter the id: "))
	emp_age=int(input("enter the age: ")) 
	emp_salary=int(input("enter the salary: "))

	if emp_id in sup_id:
		sup=Supervisor(emp_name,emp_id,emp_age,emp_salary)
	else:  
		emp=Employee(emp_name ,emp_id,emp_age,emp_salary)

		
	
	if choice==1:
		months=int(input("enter number of months: "))
		if emp_id in sup_id:
			tot_salary=sup.salary(months)
			print(tot_salary)
		else:
			tot_salary=emp.salary(months)
			print(tot_salary)


	elif choice==2:
		if emp_id in sup_id: 
			sup.disp_details()
		else:
			emp.disp_details()

	elif choice==3:
		if emp_id in sup_id:
			sup.check()
		else:
			emp.check()
	
	elif choice==4:
		if emp_id in sup_id:
			sup.calc_tax()
		else:
			emp.calc_tax()		
		
	else:
		break







