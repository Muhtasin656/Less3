money=1000
print("you have bought items worth 1000 but you do not have exact 1000 ")
cash_entered=int(input("enter how much money you have (has to be above 1000):"))
cash_returned=cash_entered-money
print(f"{cash_returned} is your change")