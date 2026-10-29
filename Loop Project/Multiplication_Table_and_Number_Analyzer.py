
#  Multiplication Table and Number Analyzer

print("=== PART 1: MULTIPLICATION TABLE ===")

table_num = int(input("Enter a positive integer for the multiplication table: "))


print(f"\nMultiplication Table for {table_num}:")
print("-" * 30)
for i in range(1, 11):
    product = table_num * i
    print(f"{table_num} x {i:<2} = {product}")



print("\nNUMBER RANGE ANALYZER")

while True:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    

    if start <= end:
        break
    else:
        print("❌ Validation Error: Start cannot be greater than end. Please try again.\n")

even_count = 0
odd_count = 0
range_sum = 0


for num in range(start, end + 1):
    range_sum += num  
    

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print("\n" + "=" * 40)
print("          RANGE ANALYSIS REPORT         ")
print("=" * 40)
print(f"Range Analyzed       : {start} to {end}")
print(f"Even Numbers Count   : {even_count}")
print(f"Odd Numbers Count    : {odd_count}")
print(f"Sum of Range         : {range_sum}")
print("=" * 40)