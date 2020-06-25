#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def load_salary_data(path_to_datarecord):
    '''
    load salary-related data from file
    returns list of user data dictionaries
    '''

    emp_database = []

    try:
        with open(path_to_datarecord, 'r') as record:
            data = record.readlines()
            for dp in data:
                dp.replace("\n", "")
                emp_database.append(eval(dp))
    except:
        print("Unable to load file.")

    return emp_database


def log_salary(log_entry):
    '''
    create a log entry of payment made
    '''
    try:
        with open("salary_payments.txt", 'a') as log:
            log.write(log_entry)

    except:
        print("Unable to load file.")


def pay_Salary(path_to_datarecord):
    entries = load_salary_data(path_to_datarecord)

    for entry in entries:
        key = list(entry.keys())[0]
        annual_sal = entry.get(key).get('Annual Salary')
        log_salary("Payment: Rs.{:.2f} to empId:{}\n".format(int(annual_sal //12), key))
    print("Payment of Employee" + entry.get(key).get('Name') + str(annual_sal//12))

    # pay saslary to employees in record


