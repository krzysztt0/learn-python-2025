def vending_machine():
    cans=int(input(f'how many cans would you like?: '))
    price= int(cans)*25
    output_price=print(f'you have to pay {price}kr')
    coins=[1,2,5,10,20]

    balance=0
    while balance<price:
        coin=int(input("inser coin:(1,2,5,10,20)"))
        if coin in coins:
            balance+=coin
        else:
            print("there is such a not coin like that")
        
    
    print(f'you paid{balance}DKK, and you are buying{cans} cans.')
    change=balance-price

    if change>0:
        print(f'your change is {change}dkk')


