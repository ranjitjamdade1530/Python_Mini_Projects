
# Password Strength Checker

password = input("Enter your password to check strength: ")


has_upper = False
has_lower = False
has_digit = False
has_special = False


for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True


is_long_enough = len(password) >= 8


criteria_met_count = sum([is_long_enough, has_upper, has_lower, has_digit, has_special])


if is_long_enough and has_upper and has_lower and has_digit and has_special:
    strength = "Strong"
    feedback = "Excellent! Your password meets all security criteria."
elif len(password) >= 6 and criteria_met_count >= 3:
    strength = "Medium"
    feedback = "Moderate. Consider adding more security elements (uppercase, digits, or special characters)."
else:
    strength = "Weak"
    feedback = "Weak! Your password is too short or lacks diverse character types."


print("\n" + "=" * 45)
print("         PASSWORD STRENGTH REPORT        ")
print("=" * 45)
print(f"Password Length (>= 8) : {'✔ Pass' if is_long_enough else '❌ Fail'} ({len(password)} characters)")
print(f"Uppercase Letter       : {'✔ Yes' if has_upper else '❌ No'}")
print(f"Lowercase Letter       : {'✔ Yes' if has_lower else '❌ No'}")
print(f"Digit (0-9)            : {'✔ Yes' if has_digit else '❌ No'}")
print(f"Special Character      : {'✔ Yes' if has_special else '❌ No'}")
print("-" * 45)
print(f"Overall Strength       : {strength}")
print(f"Feedback               : {feedback}")
print("=" * 45)