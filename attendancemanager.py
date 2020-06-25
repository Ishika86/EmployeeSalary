import employee
def attendace_manager(entries):
    try:
        choice=int(input(("Enter type of leave:\n 1.Leisure Leave\n 2.Medical Leave ")))
        if choice == 1:
            leisure(entries)
        elif choice == 2:
            medical(entries)
        else:
            print("Invalid choice ")
            attendace_manager(entries)
    except ValueError:
        print("Enter integer")

def leisure(entries):
    max_leave=2
    for entry in entries:
        for i in entry:
            emp_name = entry.get(i).get("Name")
            annual_salary = entry.get(i).get("Annual Salary")
            monthly_sal=annual_salary/12
            try:
                day_off = int(input("Number of Leave taken: "))
                if day_off < max_leave or day_off == max_leave:
                    return monthly_sal
                else:
                    cut_off = int(input("Enter per day deduction Rs:"))
                    monthly_sal -= (day_off-max_leave)*cut_off
                    entry["Monthly Salary"] = monthly_sal
                    print("The monthly salary for employee",entry.get(i).get("Name"),"is",monthly_sal)
                    return monthly_sal
            except ValueError:
                print("Invalid entry")


def medical(entries):
    for entry in entries:
        for i in entry:
            annual_salary = entry.get(i).get("Annual Salary")
            monthly_sal= annual_salary / 12
            try:
                insurance_amt= int(input("Enter insurance amount Rs:"))
                gross_sal = insurance_amt+ monthly_sal
                return gross_sal
            except:
                print("Invalid entey")


def monthly_attendance(entries):
    f = open('C:/Users/Lenovo/Desktop/registry.txt.txt', 'a')
    log_detail = {}
    detail = []
    text = []
    for entry in entries:
        empName = entry.get("Name")
        print(empName)
        n = int(input("How many days you want to register:"))
        for i in range(n):
            text.append(input(" Active or day off:"))
        log_detail = {"Name": empName, "Attendance": text}
        detail.append(log_detail)
        f.write(str(detail))







