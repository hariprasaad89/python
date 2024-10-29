#palindrome
number=int(input("Enter the number to check palindrome or not"))
rev=str(number)[::-1]
if int(rev)==number:
    print("palindrome")
else:
    print("not an palindrome")