def calculate_change(bill, paid):
    return paid - bill

total_bill = 2.50
amount_paid = 4.00

change = calculate_change(total_bill, amount_paid)
print(f"Change to return: ${change:.2f}")

