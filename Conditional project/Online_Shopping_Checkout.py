
# Online Shopping Checkout

customer_name = input("Enter Customer Name: ")
purchase_amount = float(input("Enter Purchase Amount: ?"))
customer_type = input("Enter Customer Type (Regular/Premium): ").strip().capitalize()


discount_percentage = 0.0


if purchase_amount >= 1000:
   
    if purchase_amount >= 5000:
        discount_percentage = 20.0
    else:
        if purchase_amount >= 3000 and purchase_amount < 5000:
            discount_percentage = 10.0
        else:
            discount_percentage = 5.0
else:
    discount_percentage = 0.0


if customer_type == "Premium":
    if purchase_amount >= 1000 or discount_percentage > 0:
        discount_percentage += 5.0
    else:
       
        discount_percentage += 5.0


discount_amount = (purchase_amount * discount_percentage) / 100
amount_after_discount = purchase_amount - discount_amount


delivery_charge = 0.0
if amount_after_discount >= 2000:
    delivery_charge = 0.0
else:
   
    if amount_after_discount < 2000 and amount_after_discount >= 0:
        delivery_charge = 100.0
    else:
        delivery_charge = 100.0


final_payable_amount = amount_after_discount + delivery_charge


print("\n" + "="*40)
print("         ONLINE SHOPPING RECEIPT        ")
print("="*40)
print(f"Customer Name        : {customer_name}")
print(f"Customer Type        : {customer_type}")
print(f"Purchase Amount      : {purchase_amount:.2f}")
print(f"Discount Amount      : {discount_amount:.2f} ({discount_percentage}%)")
print(f"Delivery Charge      : {delivery_charge:.2f}")
print(f"Final Payable Amount : {final_payable_amount:.2f}")
print("="*40)