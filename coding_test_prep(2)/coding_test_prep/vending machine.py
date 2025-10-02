def vending_machine():
    can=25
    coins=[1,2,5,10,20]
    
cans=int(input("How many cans would you like?"))
cost= 25*cans
print(f"The total cost is {cost} kr.")


paid=0
while paid<total_cost:
    coin = int(input("Insert coin (1, 2, 5, 10, 20 kr): "))
    if coin not in coins:
        print("Error: Invalid coin.")
    else:
        paid += coin
        print(f"Current balance: {paid} kr")

        change = paid - total_cost
    print(f"Paid: {paid} kr")
    print(f"Cans bought: {cans}")
    if change > 0:
        print(f"Change: {change} kr")