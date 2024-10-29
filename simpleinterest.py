#Find the simple interest
#SI = p*n*r/100
principle=int(input("enter the principle"))
noofyears=int(input("enter the no of years"))
rateofinterest=int(input("enter the rate of interest"))
si=float((principle*noofyears*rateofinterest)/100)
total_amount=si+principle
print("total amount {} to be paid for {} years at rate of {}".format(total_amount,noofyears,rateofinterest))