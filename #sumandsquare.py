#program that will take three digits from the user and add the square of each digit
number1=(input("Enter the number"))
sum=0
for i in str(number1):
    sum=sum+(int(i)**2)
print (sum)