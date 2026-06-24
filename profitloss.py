potato = float(input("please enter product price"))

saleprice = float(input("please enter the sales price"))

if saleprice > potato:
    amount = saleprice - potato
    print(amount, "The profit")
else:
    print("Loss of profit")