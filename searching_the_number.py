#searching the number in the list
sd=[4,5,6,2,3,9,1,4,5,6,3]
n=int(input("Enter the number to search in the given list"))
for i in sd:
    if n==i:
        print("{} is present".format(i))
        break
else:
    print("Number is not present")