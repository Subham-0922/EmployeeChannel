employees=[
    {'name':'John','salary':3000,'designation':'developer'},
    {'name':'Emma','salary':4000,'designation':'manager'},
    {'name':'Kelly','salary':3500,'designation':'tester'}

]
def getMaxSalaryEmployee(arr):
    max=0
    employee=None
    for emp in arr:
        if emp['salary']>max:
            max=emp['salary']
            employee=emp;
    return employee;
print(getMaxSalaryEmployee(employees))
