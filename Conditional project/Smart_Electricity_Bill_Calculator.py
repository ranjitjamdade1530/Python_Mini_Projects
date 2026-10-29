
#  Smart Electricity Bill Calculator


customer_name = input("Enter Customer Name: ")
units_consumed = float(input("Enter Units Consumed: "))

energy_charge = 0.0
service_charge = 150.0

if units_consumed <= 100:
    energy_charge = units_consumed * 3
elif units_consumed <= 200:
 
    if units_consumed > 100:
        energy_charge = (100 * 3) + ((units_consumed - 100) * 5)
else:
    
    energy_charge = (100 * 3) + (100 * 5) + ((units_consumed - 200) * 7)


final_bill = energy_charge + service_charge

usage_message = ""
if final_bill > 5000:
    usage_message = "High Usage Bill"
else:
    
    if final_bill > 2000:
        usage_message = "Moderate Usage Bill"
    else:
        usage_message = "Normal Usage Bill"


print("\n" + "="*35)
print("       ELECTRICITY BILL STATEMENT      ")
print("="*35)
print(f"Customer Name  : {customer_name}")
print(f"Units Consumed : {units_consumed}")
print(f"Energy Charge  : {energy_charge:.2f}")
print(f"Service Charge : {service_charge:.2f}")
print(f"Final Bill     : {final_bill:.2f}")
print(f"Usage Message  : {usage_message}")
print("="*35)