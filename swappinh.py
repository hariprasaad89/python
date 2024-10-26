# Swap the number without using third varible
number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))
print("before swapping" , number1,number2)
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print("after swapping" , number1,number2)
