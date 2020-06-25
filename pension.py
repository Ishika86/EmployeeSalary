def set_Pension(entries):
     for entry in entries:
        for i in entry:
            file_t=open('C:/Users/Lenovo/Desktop/pension.txt','a+')  
            ann_sal=entry.get(i).get("Annual Salary")
            pension_amount = ann_sal * 0.08
            t=entry.get(i)
            t["Pension"] = pension_amount
            print("The pension for employee", t["Pension"])

        print()