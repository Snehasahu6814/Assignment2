from faker import Faker  
import pandas as pd
from openpyxl import workbook

fake=Faker()
employee_list=[]
low_salary_row=""
gkk=''

for i in range (5):
       Emp_name= fake.name()
       Emp_Email=fake.email()
       Emp_id=fake.unique.random_number(digits=4)
       Emp_Salary=fake.random_number(digits=5)
       Emp_BU=fake.random_element(elements=("HR","FINANCE","IT","Sales","Developer"))
       employee_list.append([Emp_name,Emp_Email,Emp_id,Emp_Salary,Emp_BU]) 
    # return employee_list
        
df = pd.DataFrame(employee_list, columns=["Emp_name","Emp_Email","Emp_id","Emp_Salary","Emp_BU"])

# Save DataFrame to Excel
df.to_excel("Employee_Personal_Details.xlsx", index=False)
# df = pd.read_excel("Employee_Personal_Details.xlsx")
#  WAF to return the Business Unit with top most aggregated salary
def Top_Salary():
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    max_salary_row = df[df['Emp_Salary'] == df['Emp_Salary'].max()]
    # print(max_salary_row)
    return max_salary_row['Emp_name'].iloc[0]
print("max_salary Employee Name is: " ,Top_Salary())
# data1=''
# def get_employee_with_less_salary(): 
#     df = pd.read_excel("Employee_Personal_Details.xlsx")
#     max_salary_row = df[df['Emp_Salary'] == df['Emp_Salary'].min()]
#     return max_salary_row['Emp_name'].iloc[0]
 
#  WAF to return the Business Unit with top most aggregated salary
def get_business_unit_with_top_salary():  # b
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    top_business_unit = df.groupby('Emp_BU')['Emp_Salary'].sum().idxmax()
    return top_business_unit
 
#  WAF to return the employee name in each Business Unit with top most salary
def get_employee_with_top_salary_in_each_unit():  #c
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    result = {}
    for unit in df['Emp_BU'].unique():
        unit_df = df[df['Emp_BU'] == unit]
        max_salary_row = unit_df[unit_df['Emp_Salary'] == unit_df['Emp_Salary'].max()]
        result[unit] = max_salary_row['Emp_name'].iloc[0]
    return result
 
#  WAF Delete the Record of the Employee name from the Excel File with the least salary.
def  Delete_the_record_of_the_Employee ():  #d
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    min_salary_row = df[df['Emp_Salary'] == df['Emp_Salary'].min()]
    df.drop(min_salary_row.index, inplace=True)
    df.to_excel("Employee_Personal_Details.xlsx", index=False)
#  WAF to Update the Salary Details of an Employee in the Excel File
 
def update_employee_salary(emp_name, new_salary): #e
    df = pd.read_excel("Employee_Personal_Details.xlsx")
    df.loc[df['Emp_name'] == emp_name, 'Emp_Salary'] = new_salary
    df.to_excel("Employee_Personal_Details.xlsx", index=False)
 
# Testing the functions
print("Employee with top most salary:", Top_Salary())
# print("Employee with less most salary:", get_employee_with_less_salary())
print("Business Unit with top most aggregated salary:", get_business_unit_with_top_salary())
print("Employee with top most salary in each Business Unit:", get_employee_with_top_salary_in_each_unit())
Delete_the_record_of_the_Employee ()
update_employee_salary("Mr. Joshua Carroll", 65000)
