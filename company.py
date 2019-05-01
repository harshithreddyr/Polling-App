class Employee:
	
	def __init__(self,emp_name,emp_id,emp_age,emp_salary):
		self.emp_name=emp_name
		self.emp_id=emp_id
		self.emp_age=emp_age
		self.emp_salary=emp_salary
  
	def salary(self,month):
		if not month<0:
			tot_salary=self.emp_salary*month
			print(tot_salary)
			return tot_salary
		else:
			print("enter a valied number")

	def disp_details(self):
		print("Name:{} \nEmployee ID: {} \nAge: {} \nMonthly Salary: {}".format(self.emp_name,self.emp_id,self.emp_age,self.emp_salary))

	def check(self):
		emp_avail_id = [1,2,3,4,5,6,7,8,9]
		if self.emp_id in emp_avail_id:
	  		print("employee is present")
		else:
	  		print("employee is not present ")
	
	def calc_tax(self):
		tax = self.emp_salary*0.15
		print("the tax to be payed is {}".format(tax))


			

class Supervisor(Employee):
	def salary(self,month):
		if month>4:
			tot_salary=(month-4)*self.emp_salary*1.2

			print(tot_salary)
		else:
			print("enter a valid number")


	def disp_details(self):
		print("Name:{}\nEmployee ID:{} \nAge: {}\nMonthly Salary:{}".format(self.emp_name,self.emp_id,self.emp_age,self.emp_salary))	

	def calc_tax(self):
		tax = self.emp_salary*0.25
		print("the tax to be payed is {}".format(tax))	

	def check(self):
		emp_avail_id = [1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19]
		if self.emp_id in emp_avail_id:
	  		print("employee is present")
		else:
	  		print("employee is not present ")

  




	 


	