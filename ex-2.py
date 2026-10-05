name=input("Employee Name: ")
basic=float(input("Basic Salary: "))
allowance=float(input("Allowance: "))

gross=basic+allowance

if gross<=30000:
    tax_rate=0
elif gross<=50000:
    tax_rate=0.05
elif gross<=80000:
    tax_rate=0.10
else:
    tax_rate=0.15

tax=gross*tax_rate
net_salary=gross-tax

print("\nEmployee:",name)
print("Gross Salary:",gross)
print("Tax:",tax)
print("Net Salary:",net_salary)