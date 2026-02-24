#Grocery Billing System

total = 0  # Variable to store total amount

# Repeat 5 times for 5 items
for i in range(1, 6):
    print("\nItem", i)
    
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    total = total + (price * quantity)  # Add cost to total

discount = 0  # Initially no discount

# Check if discount applies
if total > 100:
    discount = total * 0.10  # 10% discount

final_amount = total - discount  # Calculate final amount

# Display results
print("\n----- BILL -----")
print("Original Total: Rs.", total)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)
