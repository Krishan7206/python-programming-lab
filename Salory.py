salary = float(input("Enter the  salary of the employee: "))

if salary <= 10000:
    hra_percentage = 20
    da_percentage = 80
elif salary <= 20000:
    hra_percentage = 25
    da_percentage = 90
else:
    hra_percentage = 30
    da_percentage = 95
    
hra = (hra_percentage / 100) * salary
da = (da_percentage / 100) * salary

gross_salary = salary + hra + da

print(f"Gross Salary: {gross_salary:.2f}")
