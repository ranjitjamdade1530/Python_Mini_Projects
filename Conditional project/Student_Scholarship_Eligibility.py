
#  Student Scholarship Eligibility


student_name = input("Enter Student Name: ")
percentage = float(input("Enter Percentage (%): "))
annual_income = float(input("Enter Annual Family Income (₹): "))
attendance = float(input("Enter Attendance (%): "))

eligibility_status = ""
scholarship_category = "None"
reason = "None"

basic_conditions_met = (percentage >= 75) and (annual_income <= 400000) and (attendance >= 75)

if basic_conditions_met:
    eligibility_status = "Eligible"
    

    if (percentage >= 90) and (basic_conditions_met):
        scholarship_category = "Full Scholarship"
    else:
        scholarship_category = "Partial Scholarship"
        
    reason = "All basic criteria successfully met."

else:
    eligibility_status = "Not Eligible"
    scholarship_category = "Not Applicable"
    
   
    if (percentage < 75) and (annual_income > 400000) and (attendance < 75):
        reason = "Failed all criteria: Low percentage, high income, and low attendance."
    elif (percentage < 75) and (annual_income > 400000):
        reason = "Percentage is below 75% and Annual family income exceeds ₹4,00,000."
    elif (percentage < 75) and (attendance < 75):
        reason = "Percentage is below 75% and Attendance is below 75%."
    elif (annual_income > 400000) and (attendance < 75):
        reason = "Annual family income exceeds ₹4,00,000 and Attendance is below 75%."
    elif percentage < 75:
        reason = "Percentage is below 75% (Minimum required: 75%)."
    elif annual_income > 400000:
        reason = "Annual family income exceeds ₹4,00,000 (Maximum allowed: ₹4,00,000)."
    elif attendance < 75:
        reason = "Attendance is below 75% (Minimum required: 75%)."


print("\n" + "="*42)
print("      SCHOLARSHIP ELIGIBILITY REPORT    ")
print("="*42)
print(f"Student Name         : {student_name}")
print(f"Percentage           : {percentage}%")
print(f"Annual Income        : {annual_income:,.2f}")
print(f"Attendance           : {attendance}%")
print("-" * 42)
print(f"Eligibility Status   : {eligibility_status}")
print(f"Scholarship Category : {scholarship_category}")
print(f"Reason               : {reason}")
print("="*42)