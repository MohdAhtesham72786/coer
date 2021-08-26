import pymysql
connection=pymysql.connect(host='localhost',
							db='nitin',
							user='mohd123',
							password='mohd123')
cur=connection.cursor()
def createRecord():
	try:
		name=input("Enter the Name of Employee :  ")
		salary=int(input("Enter the Salary :  "))
		dsg=input("Enter the Designation : ")
		city=input("Enter the City : ")
		state=input("Enter the State : ")
		cur.execute("insert into employee(name,salary,dsg,city,state) values('{}','{}','{}','{}','{}')".format(name,salary,dsg,city,state))
		connection.commit()
		print("Record inserted!!!!\n")
	except:
		print("Please Enter a Valid Record!!!!\n")
def display():
	cur.execute("select * from employee")
	data=cur.fetchall()
	print("Eid\tName                Salary\tDesignation City           State")
	for i in data:
		print("%d\t%-20s%d\t%-12s%-15s%s"%(i[0],i[1],i[2],i[3],i[4],i[5]))
	print()
def search():
	try:
		num=int(input("Enter the Employee Id to Search a Record : "))
		cur.execute("select * from employee where eid=%d"%num)
		data=cur.fetchone()
		if(data is None):
			print("No Record Found!!!!\n")
		else:
			print("Eid\tName                Salary\tDesignation City           State")
			print("%d\t%-20s%d\t%-12s%-15s%s\n"%(data[0],data[1],data[2],data[3],data[4],data[5]))
	except:
		print("Please Enter a valid Employee Id!!!!\n")		
def edit():
	try:
		num=int(input("Enter the Employee Id to Edit a Record : "))
		cur.execute("select * from employee where eid=%d"%num)
		data=cur.fetchone()
		if(data is None):
			print("No Record Found!!!!\n")
		else:
			salary=int(input("Enter the Salary to Update :  "))
			cur.execute("update employee set salary=%d where eid=%d"%(salary,num))
			print("Employee Record Updated Successfully!!!!\n")
			connection.commit()
	except:
		print("Please Enter a valid Employee Id!!!!\n")	
def delete():
	try:
		num=int(input("Enter the Employee Id to Delete a Record : "))
		cur.execute("select * from employee where eid=%d"%num)
		data=cur.fetchone()
		if(data is None):
			print("No Record Found!!!!\n")
		else:
			cur.execute("delete from employee where eid=%d"%num)
			print("Employee Record Deleted Successfully!!!!\n")
			connection.commit()
	except:
		print("Please Enter a valid Employee Id!!!!\n")	
while(True):
	try:
		choice=int(input("MySql Connect CRUD\n1. Create a Record\n2. Display all Record\n3. Search a Record\n4. Edit a Record\n5. Delete a Record\n6. Exit\nEnter Your choice : "))
		if(choice==1):
			createRecord()
		elif(choice==2):
			display()
		elif(choice==3):
			search()
		elif(choice==4):
			edit()
		elif(choice==5):
			delete()
		elif(choice==6):
			connection.close()
			break
		else:
			print("Invalid choice")
	except:
     print("please enter a valid choice!!!!!\n")         
		

