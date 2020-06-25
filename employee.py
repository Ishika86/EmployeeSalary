import re
def employeeData():
   
    total_entries=[]
    diction={}
    entries= []
    email_pattern='\S+@\S+'
    pass_pattern='[A-Za-z0-9@#$%^&+=]{8,}'
    file_s=open('C:/Users/Lenovo/Desktop/Isha.txt.txt','r')   #Open the file in read mode to know id available
    trial={}
    for line in file_s.readlines():
        total_entries.append(line[2:line.find(':')-1])                                            # Store all the id's available in a file in a list
    #print(total_entries)
    print("How many entries you want to add:")                  
    n=int(input())                                              # If no entries to add then it will exit 
    if n==0:
        exit
    else:
        while(n>0):
            file_t=open('C:/Users/Lenovo/Desktop/Isha.txt.txt','a+')    #Open the file for reading and appending 
            empId=input("Enter the Employee Id:")
            if(empId in total_entries):                                    # If emp id already exists ask for new id
                print("Employee Id already exists")
            else:                                                     # If not there add into the file
                empName=input("Enter the Employee Name: ")
                department=input("Enter the Employee Department: ")
                while True:
                    try:
                        experience=int(input("Enter the experience period : "))
                    except ValueError:
                        print("Please enter integer value") 
                        experience=int(input("Enter the experience period: "))  
                        continue
                    else:
                        break 
                while True:
                    try:
                        annual_salary=int(input("Enter the Annual salary : "))
                    except:
                        print("Please enter integer value")   
                        continue
                    else:
                        break
                empEmail=input("Enter the Email Id :")   
                while (not re.search(email_pattern,empEmail)):
                    print("Please Enter valid email id ")
                    empEmail=input("Enter the Email Id : ") 
                empPass=input("Enter the Password")   
                while (not re.search(pass_pattern,empPass)):
                    print("Please enter strong password minimum of length 8 which contains uppercase,lowercase,digits and special character")
                    empPass=input("Enter the Password : ")                         
                diction={"Name" : empName,"Department" : department, "Experience" : experience,"Annual Salary": annual_salary,"EmailId":empEmail,"Password":empPass}
                trial={empId : diction}
                entries.append(trial)
                file_t.write(str(trial))                        #Appending the dictionary in string format in a file
                file_t.write('\n')
                total_entries.append(empId)                     # Append the new emp id in the total_entries so if 
                n=n-1                                           #recently added emp id comes then it will say empId already exist
                #print(total_entries)
                #print(trial)
        return entries                                          # Returning all the records in a list data type
#employeeData()
  
# To add condition to check if empId already exists in a file
