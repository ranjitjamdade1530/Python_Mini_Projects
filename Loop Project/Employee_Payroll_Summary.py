
#  Employee Payroll Summary

num_employees = int(input("Enter the total number of employees: "))


total_net_payroll = 0.0

payroll_reports = []


for i in range(1, num_employees + 1):
    employee_name = input(f"Enter Employee {i}'s Name: ")
    basic_salary = float(input(f"Enter {employee_name}'s Basic Salary (₹): "))
    overtime_hours = float(input(f"Enter {employee_name}'s Overtime Hours: "))


    overtime_pay = overtime_hours * 200.0  
    gross_salary = basic_salary + overtime_pay

    if gross_salary >= 50000:
        deduction_rate = 0.10  
    else:
        deduction_rate = 0.05  

    deduction_amount = gross_salary * deduction_rate
    net_salary = gross_salary - deduction_amount

   
    total_net_payroll += net_salary

   
    payroll_reports.append((employee_name, gross_salary, deduction_amount, net_salary))


print("\n" + "=" * 65)
print("                    EMPLOYEE PAYROLL SUMMARY REPORT                ")
print("=" * 65)
print(f"{'Employee Name':<15} | {'Gross Salary':<12} | {'Deduction':<10} | {'Net Salary':<12}")
print("-" * 65)

for name, gross, deduction, net in payroll_reports:
    print(f"{name:<15} | ₹{gross:<11.2f} | ₹{deduction:<9.2f} | ₹{net:<11.2f}")

print("=" * 65)
print(f"Total Employees Processed : {num_employees}")
print(f"Total Net Payroll         : ₹{total_net_payroll:,.2f}")
print("=" * 65)