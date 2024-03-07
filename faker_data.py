"""Generating the fake data and store it in the ExcelSheet"""
import time
from faker import Faker
import pandas as pd
def log_execution_time(func):
    """log exceution"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with open("execution_logs.txt", "a",encoding="utf-8") as f:
            f.write(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds\n")
        return result
    return wrapper
#from openpyxl import workbook
fake=Faker()
employee_list=[]
#Low_Salary_Row= ""
#GKK=''
df = pd.read_excel("Employee_Personal_Details.xlsx")
for i in range (5):
    emp_name= fake.name()
    emp_Email=fake.email()
    emp_id=fake.unique.random_number(digits=4)
    emp_Salary=fake.random_number(digits=5)
    emp_BU=fake.random_element(elements=("HR","FINANCE","IT","Sales","Developer"))
    employee_list.append([emp_name,emp_Email,emp_id,emp_Salary,emp_BU])
    # return employee_list
df = pd.DataFrame(employee_list, columns=["emp_name","emp_email","emp_id","emp_salary","emp_bu"])
# Save DataFrame to Excel
df.to_excel("Employee_Personal_Details.xlsx", index=False)
# df = pd.read_excel("Employee_Personal_Details.xlsx")
#  WAF to return the Business Unit with top most aggregated salary
@log_execution_time
def top_salary():# df = pd.read_excel("Employee_Personal_Details.xlsx")
    """Returning the to most dalary using thr topmost_Salary"""
    max_salary_row = df[df['emp_salary'] == df['emp_salary'].max()]# print(max_salary_row)
    return max_salary_row['emp_name'].iloc[0]
print("max_salary Employee Name is: " , top_salary())
@log_execution_time
def get_business_unit_with_top_salary():
    """ Method for  Returning  the buisness unit with"""
    #df = pd.read_excel("Employee_Personal_Details.xlsx")
    top_business_unit = df.groupby('emp_bu')['emp_salary'].sum().idxmax()
    return top_business_unit
# WAF to return the employee name in each  Business Unit with top most salary
@log_execution_time
def get_employee_with_top_salary_in_each_unit():
    #df = pd.read_excel("Employee_Personal_Details.xlsx")
    """ Method for  Returning  the buisness unit with"""
    result = {}
    for unit in df['emp_bu'].unique():
        unit_df = df[df['emp_bu'] == unit]
        max_salary_row = unit_df[unit_df['emp_salary'] == unit_df['emp_salary'].max()]
        result[unit] = max_salary_row['emp_name'].iloc[0]
    return result
#  WAF Delete the Record of the Employee name from the Excel File with the least salary.
@log_execution_time
def delete_the_record_of_the_employee ():  #d
   # df = pd.read_excel("Employee_Personal_Details.xlsx")
    """ Method for  Returning  the buisness unit with"""
    min_salary_row = df[df['emp_salary'] == df['emp_salary'].min()]
    df.drop(min_salary_row.index, inplace=True)
    df.to_excel("Employee_Personal_Details.xlsx", index=False)
#  WAF to Update the Salary Details of an Employee in the Excel File
@log_execution_time
def update_employee_salary(emp_name,new_salary):
    """Making the function to update the salary and  food"""
    #df = pd.read_excel("Employee_Personal_Details.xlsx")
    df.loc[df['emp_name'] == emp_name, 'emp_salary'] = new_salary
    df.to_excel("Employee_Personal_Details.xlsx", index=False)
 # Testing the functions
print("Employee with top most salary:", top_salary())
# print("Employee with less most salary:", get_employee_with_less_salary())
print("Business Unit with top most aggregated salary:", get_business_unit_with_top_salary())
print("Topmost salary Employee in each BusinessUnit:", get_employee_with_top_salary_in_each_unit())
delete_the_record_of_the_employee()
update_employee_salary("Mr. Joshua Carroll", 65000)
