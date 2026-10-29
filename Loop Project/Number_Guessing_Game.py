
#  Number Guessing Game

SECRET_NUMBER = 37
max_attempts = 5
attempts_used = 0
has_won = False

print("=== Welcome to the Number Guessing Game ===")
print(f"I have picked a secret number. You have {max_attempts} attempts to guess it!\n")


while attempts_used < max_attempts:
    guess = int(input(f"Enter your guess (Attempt {attempts_used + 1} of {max_attempts}): "))
    attempts_used += 1  

    if guess == SECRET_NUMBER:
        has_won = True
        break  
    elif guess < SECRET_NUMBER:
        print("📈 Too low! Try a higher number.")
    else:
        print("📉 Too high! Try a lower number.")


print("\n" + "=" * 45)
print("             GAME OVER REPORT            ")
print("=" * 45)

if has_won:
    print(f"Status           : YOU WON! 🎉")
    print(f"Attempts Used    : {attempts_used}")
    print(f"Secret Number    : {SECRET_NUMBER}")
    print(f"Message          : Fantastic job guessing the secret number!")
else:
    print(f"Status           : YOU LOST! 😢")
    print(f"Attempts Used    : {attempts_used}")
    print(f"Secret Number    : {SECRET_NUMBER}")
    print(f"Message          : Out of attempts! Better luck next time.")

