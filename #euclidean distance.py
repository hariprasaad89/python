#euclidean distance
#formula to calc - round(math.dist(x,y),2) 

import math
x1=int(input("Enter the x coordinates"))
y1=int(input("Enter the y coordinates"))
x2=int(input("Enter the x coordinates"))
y2=int(input("Enter the y coordinates"))

x=[x1,y1]
y=[x2,y2]
ed=round(math.dist(x,y),2)
print("euclidean distance" , ed)