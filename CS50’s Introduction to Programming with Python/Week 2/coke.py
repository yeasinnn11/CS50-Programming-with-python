amount_due = 50
accsepted_coin = [25,10,5]
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in accsepted_coin:
        amount_due -= coin
change_own = abs(amount_due)
print(f"Change Owed: {change_own}")
