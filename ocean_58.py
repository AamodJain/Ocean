# importing matplotlib module 
import matplotlib.pyplot as plt

# defining a function flipShift_y to flip and shift the curve along the y - axis
def flipShift_y(l):
    # iterating through the reversed list 
    for i in l[::-1]:
        # storing the x,y coordinates in x and y 
        x,y = i
        # appending the updated coordinates in arr,xlist and ylist after flipping the points
        arr.append((x,k+(k-y)-1))
        xlist.append(x)
        ylist.append(k+(k-y)-1)
    # storing the number of places to be shifted in a variable s
    s =k*2
    # iterating through l
    for i in l:
        # storing the x,y coordinates in x and y 
        x,y = i
        # appending the updated coordinates in arr,xlist and ylist after flipping the points
        arr.append((x,s+y))
        xlist.append(x)
        ylist.append(s+y)

# defining a function flipShift_x to flip and shift the curve along the x - axis
def flipShift_x(l):
    # iterating through the reversed list
    for i in l[::-1]:
        # storing the x,y coordinates in x and y 
        x,y = i
        # appending the updated coordinates in arr,xlist and ylist after flipping the points
        arr.append((k+(k-x)-1,y))
        xlist.append(k+(k-x)-1)
        ylist.append(y)
    # storing the number of places to be shifted in a variable s
    s =k*2
    for i in l:
        # storing the x,y coordinates in x and y
        x,y = i
        # appending the updated coordinates in arr,xlist and ylist after flipping the points
        arr.append((s+x,y))
        xlist.append(s+x)
        ylist.append(y)

# taking n as input from the user
n = int(input('Enter the value of n :'))

# initializing l with the coordinates of the first four points
l = [(0,0),(0,2),(1,2),(1,0),(2,0),(2,2)]

#creating a list arr to hold the coordinates of all the points in the pattern
arr = list(l)

# creating xlist and ylist to hold the x and y coordinates of the points respectively
xlist,ylist = [0,0,1,1,2,2],[0,2,2,0,0,2]

# creating a variable k
k = 3

# calling flipShift functions recursively to produce the desired patterns
for i in range(2, n+1):

    flipShift_y(l)
    l = list(arr)

    flipShift_x(l)
    l = list(arr)

    # updating the val. of k
    k*=3

# plotting and showing the peano curve
plt.plot(xlist,ylist)
plt.show()


        
