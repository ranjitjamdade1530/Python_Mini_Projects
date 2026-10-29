
#  ATM PIN Verification

CORRECT_PIN = "1234"
max_attempts = 3
attempts_used = 0
access_granted = False

print("=== Welcome to the Automated Teller Machine ===")

while attempts_used < max_attempts:
    entered_pin = input(f"Enter your 4-digit PIN (Attempt {attempts_used + 1} of {max_attempts}): ")
    attempts_used += 1  


    if entered_pin == CORRECT_PIN:
        access_granted = True
        break  
    else:
        print("❌ Incorrect PIN.")

print("\n" + "=" * 40)
print("           ATM ACCESS REPORT            ")
print("=" * 40)

if access_granted:
    print(f"Access Status    : Access Granted")
    print(f"Attempts Used    : {attempts_used}")
    print(f"Message          : Welcome! Please proceed with your banking.")
else:
    print(f"Access Status    : Access Denied")
    print(f"Attempts Used    : {attempts_used}")
    print(f"Lock Message     : Card Temporarily Locked")

print("=" * 40)