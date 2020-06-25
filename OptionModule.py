import employee
import sys
import re
import attendancemanager as am
import pension 
import payments 
import taxmanager as t
import ast
import employee
def options():
    total_entries=[]
    total_password=[]
    pattern='[1234]'
    file_s=open('C:/Users/Lenovo/Desktop/Isha.txt.txt','r')
    while True:
        print("Enter ur choices:")
        print("1. Add Employee Details ")
        print("2. Display existing Employee Details")
        print("3. Exit")
        n=int(input())
        if(re.search(pattern,str(n))):
            if(n==1):
              emp=employee.employeeData()
              am.attendace_manager(emp)
              am.monthly_attendance(emp)
              t.taxmanager(emp)
              pension.set_Pension(emp)
              payments.pay_Salary('C:/Users/Lenovo/Desktop/Isha.txt.txt')   
                            
            elif (n==2):
                employee_id=input("Enter Employee Id of Employee : ")
                employee_password=input("Enter Password of employee : ")
                for line in file_s.readlines():
                    total_entries.append(line[2:line.find(':')-1]) 
                    total_password.append(line[line.rindex(':')+3:line.rindex('\'')])
                print(total_password)
                print(employee_id)
                print(total_entries[int(employee_id)-1])
                print(total_password[int(employee_id)-1])
                print(employee_password)
                if(employee_id == total_entries[int(employee_id)-1] and total_password[int(employee_id)-1] == employee_password):
                    file_t=open('Isha.txt.txt','r')
                    data=file_t.readlines()
                    print(data[int(employee_id)-1])
                    break
                else:
                    print("Employee data is not there")   
                    break 
            elif(n==3):
                sys.exit
                break    
            else:
                print("Please enter valid input")

options()