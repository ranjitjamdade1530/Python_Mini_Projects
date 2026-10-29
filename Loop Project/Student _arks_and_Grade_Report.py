
#  Student Marks and Grade Report

num_students = int(input("Enter the total number of students: "))


total_marks = 0.0
pass_count = 0
fail_count = 0


student_reports = []

for i in range(1, num_students + 1):
    
    student_name = input(f"Enter Student {i}'s Name: ")
    
   
    while True:
        marks = float(input(f"Enter {student_name}'s Marks (out of 100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid marks! Marks must be between 0 and 100. Please try again.")

   
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"


    total_marks += marks  
    
    if marks >= 40:
        pass_count += 1   
    else:
        fail_count += 1   


    student_reports.append((student_name, marks, grade))

if num_students > 0:
    class_average = total_marks / num_students
else:
    class_average = 0.0


print("\n" + "=" * 50)
print("             CLASS PERFORMANCE REPORT             ")
print("=" * 50)
print(f"{'Student Name':<20} | {'Marks':<8} | {'Grade':<6}")
print("-" * 50)

for name, m, g in student_reports:
    print(f"{name:<20} | {m:<8.2f} | {g:<6}")

print("=" * 50)
print(f"Total Students Processed : {num_students}")
print(f"Class Average Marks      : {class_average:.2f}%")
print(f"Total Passed Students    : {pass_count}")
print(f"Total Failed Students    : {fail_count}")
print("=" * 50)