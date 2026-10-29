
# Employee Performance Bonus

employee_name = input("Enter Employee Name: ")
monthly_salary = float(input("Enter Monthly Salary (₹): "))
years_experience = int(input("Enter Years of Experience: "))
performance_rating = int(input("Enter Performance Rating (1 to 5): "))


valid_input = True
error_message = ""
bonus_percentage = 0.0
performance_message = ""

if performance_rating < 1 or performance_rating > 5:
    valid_input = False
    error_message = "Error: Invalid rating entered. Performance rating must be between 1 and 5."
else:
    if performance_rating == 5:
        performance_message = "Excellent Performer"
    elif performance_rating == 4:
        performance_message = "Good Performer"
    elif performance_rating == 3:
        performance_message = "Satisfactory Performer"
    else:
        performance_message = "Needs Improvement"

    if performance_rating < 3:
        bonus_percentage = 0.0
    elif years_experience >= 10 and performance_rating >= 4:
        bonus_percentage = 20.0
    elif years_experience >= 5 and performance_rating >= 4:
        bonus_percentage = 15.0
    elif years_experience >= 2 and performance_rating >= 3:
        bonus_percentage = 10.0
    else:
        bonus_percentage = 0.0

annual_base_salary = monthly_salary * 12
bonus_amount = (monthly_salary * bonus_percentage) / 100
final_monthly_salary = monthly_salary + bonus_amount

print("\n" + "="*42)
print("       EMPLOYEE BONUS & SALARY REPORT   ")
print("="*42)

if valid_input:
    print(f"Employee Name        : {employee_name}")
    print(f"Experience           : {years_experience} years")
    print(f"Performance Rating   : {performance_rating}/5")
    print(f"Performance Message  : {performance_message}")
    print("-" * 42)
    print(f"Monthly Base Salary  : {monthly_salary:,.2f}")
    print(f"Bonus Percentage     : {bonus_percentage}%")
    print(f"Bonus Amount         : {bonus_amount:,.2f}")
    print(f"Final Salary (Month) : ₹{final_monthly_salary:,.2f}")
else:
    print(f"Employee Name        : {employee_name}")
    print(f"Status               : PROCESSING FAILED")
    print(f"Reason               : {error_message}")

print("="*42)