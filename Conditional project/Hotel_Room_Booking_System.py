
# Hotel Room Booking System


guest_name = input("Enter Guest Name: ")
room_type = input("Enter Room Type (Standard, Deluxe, Suite): ").strip().title()
nights = int(input("Enter Number of Nights: "))


valid_booking = True
error_message = ""
rate_per_night = 0.0
room_charge = 0.0
discount_percentage = 0.0
discount_amount = 0.0
final_booking_amount = 0.0

if nights > 0:

    if room_type == "Standard":
        rate_per_night = 2000.0
    elif room_type == "Deluxe":
        rate_per_night = 3500.0
    elif room_type == "Suite":
        rate_per_night = 6000.0
    else:
        valid_booking = False
        error_message = "Error: Invalid room type entered. Please choose Standard, Deluxe, or Suite."

    if valid_booking:
        room_charge = rate_per_night * nights

 
        if nights >= 5:
            if nights >= 10:
                discount_percentage = 20.0
            else:
                discount_percentage = 10.0
        else:
            discount_percentage = 0.0

       
        discount_amount = (room_charge * discount_percentage) / 100
        final_booking_amount = room_charge - discount_amount

else:
    valid_booking = False
    error_message = "Error: Number of nights must be greater than 0."


print("\n" + "="*42)
print("         HOTEL BOOKING RECEIPT          ")
print("="*42)

if valid_booking:
    print(f"Guest Name           : {guest_name}")
    print(f"Room Type            : {room_type}")
    print(f"Number of Nights     : {nights}")
    print(f"Room Charge          : {room_charge:.2f}")
    print(f"Discount ({int(discount_percentage)}%)      : {discount_amount:.2f}")
    print("-" * 42)
    print(f"Final Booking Amount : ₹{final_booking_amount:.2f}")
else:
    print(f"Guest Name           : {guest_name}")
    print(f"Booking Status       : FAILED")
    print(f"Reason               : {error_message}")

print("="*42)