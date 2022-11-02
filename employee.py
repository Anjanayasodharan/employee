import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'employeedb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("1 add employee")
    print("2 view all employee")  
    print("3 search a employee")
    print("4 update the employee")   
    print("5 delete a employee")
    print("6 exit")
    choice = int(input('enter an option:'))
    if(choice==1):
        print('employee enter selected')
        empcode = input('enter the empcode')
        empname = input('enter the empname')
        designation = input('enter the designation ')
        salary = input('enter the salary')
        companyname = input('enter the company name')
        phno = input('enter the phn no')
        email = input('enter the email')
        password = input('enter the password')
        sql = 'INSERT INTO `employees`(`employeecode`, `employeename`, `designation`, `salary`, `companyname`, `phno`, `emailid`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (empcode,empname,designation,salary,companyname,phno,email,password)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        sql = 'SELECT * FROM `employees`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search employee')
    elif(choice==4):
        print('update employee')
    elif(choice==5):
        print('delete employee')
    elif(choice==6):
        break