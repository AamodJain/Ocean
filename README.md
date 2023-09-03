d# Ocean
This repository contains my solutions to the oceanverse problems .

# ocean_11
n = int(input("Enter a number :"))
def prime(x): #creating a function to check whether a given number is prime or composite
    for i in range(2,x-1):
        if x%i==0:
            break
    else:
        print(x)

for i in range(2,n+1): 
    prime(i)

# ocean_12 
# taking 2 input strings from user
s1 = input("Enter first string :")
s2 = input("Enter second string :")

print("The concatenated string is :",s1+s2)

# ocean_13
# taking 2 strings from usr
print("Enter 2 string of the same length \nInput: ")
s1 = input()
s2 = input()
n = len(s1)
ans = ''

for i in range(n):  #interspersing the second string onto the first one
    ans+=s1[i]+s2[i]

print(ans)

#ocean_14
s = input("Enter a string :")

print(s[::-1]) #using string slice to reverse the input string

#ocean_15
s = input("Enter a string :")
if s == s[::-1]: #compairing s and its reverse string 
    print(s, "is a palindrome ")
else :
    print(s, "is not a palindrome ")

# ocean_16
s = input("Enter a string :")
vowels = 'aeiou' #storing all vowels in a string
consonants = 'bcdfghjklmnpqrstvwxyz' # storing all consonants in a string
vowel_count , consonant_count = 0,0

for i in s: # checking each element of s for vowel/consonant
    if i.lower() in vowels:
        vowel_count+=1
    elif i.lower() in consonants:
        consonant_count+=1

print(f"The number of vowels in the string is : {vowel_count}")
print(f"The number of consonants in the string is : {consonant_count}")

# ocean_17
n = int(input("Enter a number :")) #taking value of n from user
print("squares of all the number from 1 to n are :-")
for i in range(1,n+1): # printing the square of all the numbers from 1-n
    print(i**2)

# ocean_18
n = int(input("Enter a number :")) #taking value of n from user
a = 0
b = 1
print(f"The first {n} terms of Fibonacci sequence are :- ")
# printing the first 2 terms 
print(a, end= ' ')
print(b, end= ' ')

# printing rest of the terms
for i in range(n-2):
    nextTerm = a+b
    a = b
    b = nextTerm
    print(nextTerm , end = ' ')

# ocean_19
n = int(input("Enter a number :")) #taking value of n from user
for i in range(n):  # varying i from 0 to n-1
    print((i+1)*"*") #printing (i+1) stars in the 'i'th row

# ocean_20
# taking the value of curvature and number of lines from the user
n = int(input("Enter the number of lines :")) 
c = float(input("Enter the value of curvature :"))

if c > 0: 
    for i in range(n//2,-1,-1): #printing 1st half of the snake
        x = int((i**2)*c) # using a formula similar to (y**2 = 4ax) to find the number of spaces required in each line 
        print(x*" ","*")  
    for i in range(n//2): # printing 2nd half of the snake
        x = int((i**2)*c)
        print(x*" ","*")

# using the same logic as above for negative curvature values 
elif c <0:
    c = abs(c) #using abs() function to get the absolute value of curvature
    for i in range(n//2,-1,-1):
        x = int(((n//2)**2)*c)-int((i**2)*c) # taking difference of max. no. of spaces and the spaces in each row to reverse the pattern
        print(x*" ","*")  
    for i in range(n//2):
        x = int(((n//2)**2)*c)-int((i**2)*c)
        print(x*" ","*")

# ocean_21
def fact(n):
    if n ==0 or n == 1: #returning 1 for fact(0) and fact(1)
        return 1
    else:
        return n*fact(n-1) # using fact(n)= n*fact(n-1)

n = int(input('Enter a number :'))
print(f'The factorial of {n} is : {fact(n)}')

# ocean_22
n = int(input('Enter a number :'))
if n>0: # if n>0 then it is +ve
    print(f'{n} is Positive')
elif n<0: # if n,0 then it is -ve
    print(f'{n} is Negative')
else : # if n=0 then it is Zero
    print(f'{n} is Zero')

# ocean_23 
p = float(input("Enter the value of Principal :"))
r = float(input("Enter the value of rate :"))
t = float(input("Enter the value of time :"))

print(f"The simple interest for the given set of principal ,rate and time is : {(p*r*t)/100}")

# ocean_24
print('Choose conversion type :-\nCelcius to Fahrenheit (Enter 1)\nFahrenheit to Celcius (Enter 2) ')
s = int(input("Enter your choice :")) # asking user's choice 
if s == 1 : # converting Celcius to Fahrenheit
    c = float(input('Enter the temperature in Celcius :'))
    f = (9/5)*c+32
    print(f"{c} Celcius = {f} Fahrenheit")
elif s == 2: # converting Fahrenheit to Celcius
    f = float(input('Enter the temperature in Fahrenheit:'))
    c = (f-32)*(5/9)
    print(f"{f} Fahrenheit = {c} Celcius")
else : # displaying a message asking user to enter a valid choice in case an invalid choice is entered
    print('Please enter a valid choice ')

# ocean_25 
n = int(input("Enter the year :")) # taking year as input from the user
# checking all the necessary conditions for an year to be a leap year
if n%4==0:
    if n%100==0:
        if n%400==0:
            print(n,'is a Leap Year')
        else : 
            print(n,'is not a Leap Year')
    else :
        print(n,'is a Leap Year')
else :
    print(n,'is not a Leap Year')

# ocean_26
# divisibility by 7 and 5
n = int(input('Enter a number :'))
if n%(7*5)==0: #checking divisibility by 7 and 5
    print(n,'is divisible by both 7 and 5')
else :
    print(n,'is not divisible by both 7 and 5')

# generalisation for a and b
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
if n%(a*b)==0: #checking divisibility by a and b entered by the user
    print(n,f'is divisible by both {a} and {b}')
else :
    print(n,f'is not divisible by both {a} and {b}')

#ocean_27
age = int(input('Enter your age :')) # taking age as input from user
# checking what group does the age entered by the user belongs to and displayig the message accordingly
if age<18: 
    print('You are a minor.')

elif age>=18 and age<65:
    print('You are an adult.')

else :
    print('You are a senior citizen.')

#ocean_28
l = [] #crDting an empty list to store the marks obtained by the student
print("Enter the marks obtained in the following subject(out of 100) :- ")
for i in range(5):
    print(f'subject {i+1} :',end= "")
    l.append(float(input())) # adding the marks of student in the list 

avg =sum(l)/5 # calculating the average marks of the student 

# Grading the student according to the average marks
if avg>=90:
    print('A Grade')
elif avg in range(80,90):
    print('B Grade')
elif avg in range(70,80):
    print('C Grade')
elif avg in range(60,70):
    print('D GrDde')
else :
    print('F Grade')

#ocean_29
n = int(input('Enter a decimal number: ')) #taking a decimal number as input from the user
ans = 0
i=0
print(f'binary representation of {n} is ', end = '')
while (n):
    bit = n&1 #finding the last bit in the binary representation of n 
    ans = (10**i)*bit + ans # using the bit obtained to form the binary representation of n
    i+=1 # incrementing i by 1
    n = n>>1 # using right shift operator in order to find the next bit 

print(ans)

# ocean_30 

# ocean_30_GCD
def gcd(a,b): # creating a function to calculate the gcd of two numbers 
    if b>a: # b should be smaller than a for the euclid's algorithm to work
        a,b=b,a
    if b==0: # if b = o , then a will be the gcd
        print(f'gcd = {a}')
    else :
        print(f'gcd({b},{a%b})') # using euclid's algorithm : gcd(a,b)=gcd(b,a%b)
        return gcd(b,a%b)

# asking user for the 2 numbers whose gcd is required
a = int(input('Enter first number :'))
b = int(input('Enter second number :'))
print(f'gcd({b},{a%b})')
gcd(a,b) # calling the gcd function 

# ocean_30_maxSteps_Basic
def gcd(a,b): # creating a function to calculate the gcd of two numbers 
    global stepCount
    if b>a: # b should be smaller than a for the euclid's algorithm to work
        a,b=b,a
    if b==0: # if b = o , then a will be the gcd and thus the gcd algorithm will end
        stepCount+=1 # incrementing the stepCount by 1 for each step
    else :
        stepCount+=1 # incrementing the stepCount by 1 for each step
        return gcd(b,a%b) # using euclid's algorithm : gcd(a,b)=gcd(b,a%b)
    
k = int(input('Enter the value of k :')) # taking the value of k from the user
max =0
ans = () # creating an empty tuple to store the required pair 
for i in range(10**(k-1),10**k):
    for j in range(i+1,10**k):
        stepCount = 0 
        gcd(i,j)
        if stepCount>max : # updating max and ans if stepCount for a pair exceeds the previous maximum value
            max = stepCount
            ans = (i,j)

print(f'required pair = {ans}')
print(f'number of steps = {max}')

# ocean_30_maxSteps_Advanced 
k = int(input('Enter the value of k :')) # taking the value of k from the user
l = [0,1] # creating a list with the first 2 terms of fibonacci sequence
a =0
b=1
nextTerm = 0
# the required pair of numbers will be the two largest k-digit numbers in the Fibonacci Sequence
while nextTerm<= 10**k: # appending all the terms less than or equal to the largest k-digit term in the fibonacci sequence in the list l
    nextTerm= a+b
    a = b
    b = nextTerm
    if nextTerm<= 10**k:
        l.append(nextTerm)

print(f'The required pair is ({l[-1]},{l[-2]})') # the two largest terms from the list l form the required pair

# ocean_31
n = int(input('Enter the value of n :')) # taking the value of n from user 
L = [i for i in range(1,n+1)] # creating a list L containing the first n natural numbers
print(L)

# ocean_32
import random # importing random module
n = random.randint(10,100) # choosing a random number as the length of the list
L = [random.randint(1,1000) for i in range(n)] # creating a list L with random numbers in the range 1-1000
print(L)

#ocean_33
def add(a,b): # creating function add
    return a+b
# taking two numbers as input from the user
a = int(input('Enter first number :'))
b = int(input('Enter second number :'))

# ocean_34
def factorial(n): # creating the function factorial
    if n ==0 or n==1 : # factorial(0) = factorial(1) = 1
        return 1 
    return n*factorial(n-1) # using factorial(n) = n*factorial(n-1)

n = int(input('Enter a number : ')) # taking n as input from the user
factorial(n) # calling factorial function

# ocean_35
def fibonacci(n): # creating fibonacci function
    a = 0
    b = 1
    if n == 1 :
        return a
    elif n == 2: 
        return b
    else :
        for i in range(n-2): 
            nextTerm = a+b # using the definition of fibonacci sequence to find the nth term 
            a = b 
            b= nextTerm
        return nextTerm

n = int(input('Enter the value of n :')) # taking n as input from user
print(f'The {n}th term of Fibonacci sequence is {fibonacci(n)}')

# ocean_36
import random # imorting random module
n = 1000000 # assuming n = 1M
l = [0 for i in range(n)] # initiating a list of length n with all elements as 0. each index in l represents an empty bin.
# simulating the process of throwing n identical balls randomly into n bins
for j in range(n):
    l[random.randint(0,999999)]+=1 # incrementing the value of a bin (value stored at that index) whenever a ball lands in it.

print(max(l)) # printing the maximum across all bins 

# ocean_37 
def balls():
    import random # imorting random module
    n = int(input("Enter the number of bins :")) # taking the number of bins as an input from the user
    l = [0 for i in range(n)] # initiating a list of length n with all elements as 0. each index in l represents an empty bin.
    count = 0 # creating a variable count to hold the value of the number of balls required
    # simulating the process of throwing balls in n bins until none of the bins remains empty
    while l.count(0)!=0:
        l[random.randint(0,n-1)]+=1 # ball gets in a random bin
        count+=1 # incrementing the value of count after every throw 
    return count # returning the number of balls required

print(balls()) # calling the function 'balls'

# ocean_38
def is_even(n): # creating is_even function
    if n%2==0: # checking if n is even or odd
        return True
    return False

n = int(input('Enter a number :')) # taking n from user as input
if is_even(n): # calling is_even function
    print(n, 'is even')

else :
    print(n, 'is odd')

# ocean_39
def circle_area(r): # creating circle_area function
    import math # importing math module
    return math.pi*(r**2) # calculating and returning the area of circle

# ocean_40
def miniSpiral(n): # creating the function miniSpiral to produce the desired pattern
    global oc,ans # using global keyword to ensure that oc and ans from the global namespace get updated
    ans+=(order[oc%4]*n) # storing the pattern in ans, one unit at a time # considering continuous string of a single letter a one unit
    oc+=1 # incrementing oc after storing one unit of the pattern
    ans+=(order[oc%4]*n) # repeating the same process for the second unit
    oc+=1 
oc = 0 # creating a variable oc to hold the current index(where storing occurs) in the string order
ans = '' # creating an empty string to hold the pattern 
order = "RULD" # defining the order as Right->Up->Left->Down
termCount=0 # creating a variable to count the number of terms printed
for i in range(1,1001): # using the loop variable i, to denote the number of times a letter has to be repeated in a unit
    miniSpiral(i) # calling the miniSpiral function

print(ans[0:1000000]) #printing the required number of terms from the pattern

# ocean_41
def concatenate(s1,s2): # creating the function concatenate
    return ' '.join([s1,s2]) # returning the concatenated string
print('enter 2 strings') # taking 2 strings as input from the user 
a = input()
b = input()
print(concatenate(a,b)) # calling the concatenate function and printing the output

# ocean_42
def find_max_1(l): # creating the find_max function
    max = l[0] # assuming l[0] to be the maximum in the list 
    for i in l:
        if i>max: 
            max = i # updating max if a number greater than max is found in the list
    return max

def find_max_2(l): # creating another function that does the same thing as find_max_1
    return max(l)

# ocean_43
def stocks(filename): # creating a function to buy and sell stocks and calculate profits
    import csv # importing csv module
    with open(filename, 'r') as f:  # opening the file through filhandle f

        fileReader = csv.reader(f) # creating a reader object to read the data from the file
        dateList,priceList = [],[] # creating 2 empty lists to hold the dates and the corresponding day ending prices
        balance = 100000 # creating a variable to hold the current balance
        i = 0 # creating a variable i to hold the position where reading is happening in the file

        for data in fileReader: # iterating through the data present in the file
            if(i):
                date = data[0] # storing the value of date
                price = float(data[4]) # storing the value of share price
                # appending these values in the designated lists
                dateList.append(date)
                priceList.append(price)

            i+=1 # incrementing the value of i
        maxPrice = (max(priceList)) # finding the max share price
        minPrice = (min(priceList)) # finding the min share price
        balance = balance%minPrice 
        # finding the appropriate date for buying and selling of shares
        buyDate = dateList[priceList.index(minPrice)]
        sellDate = dateList[priceList.index(maxPrice)]
        # printing the results
        print('buy date = ',buyDate)
        print('purchasing price =',minPrice)
        print('sell date = ',sellDate)
        print('selling price price =',maxPrice)
        print('profit = ',(((maxPrice)*(100000//minPrice))+balance - 100000))

stocks('sensexData.csv') # calling the function stocks

# ocean_44
import csv # importing csv module
import matplotlib.pyplot as plt # importing matplotlib.pyplot module as plt

with open('HeightWeight.csv') as f: # opening the file through filehandle f
    fileReader = csv.reader(f) # creating a reader object 
    i =  0 # creating a variable to store the position where reading is happening in the file 
    heightWeight = {} # creating a dict. to store height:weight pairs
    for data in fileReader: # iterating through the data present in the file
        if i: # using this condition to avoid the first row of data (['serial number' , 'height' , 'weight'])
            # extracting data from file 
            height = float(data[1])
            weight = float(data[2])
            heightWeight[height]= weight # updating the heightWeight dict.
        i+=1 # incrementing the value of i
        slope = [] # creating a list slope to store the slopes for each set of points  
    heightWeight_sorted = {} # creating a new dict. to hold the data of heightWeight sorted according to height
    for i in sorted(heightWeight.keys()):
        heightWeight_sorted[i]=heightWeight[i] # updating heightWeight_sorted
        slope.append(heightWeight_sorted[i]/i) #updating slope
    avg_slope = sum(slope)/25000 # calculating the avg. value of slope for the entire set of data
    plt.scatter(heightWeight_sorted.keys(),heightWeight_sorted.values(),color='g') # plotting the data points obtained 
    plt.plot(heightWeight_sorted.keys(),[avg_slope*height for height in heightWeight_sorted.keys()],color='r') # plotting the line denoting the average of the ratio of weight/height
    plt.scatter(heightWeight_sorted.keys(),slope,color = 'b')
    # labeling the x and y axes
    plt.xlabel('Height (in inches)')
    plt.ylabel('Weight (in pounds)')
    plt.show() # producing the graph as an output on the screen

'''
yes the data seems to be correlated . The correlation is that the ratio of weight to height (as depicted by the blue dots in the graph) is almost same for any height weight pair present in the data . Therfore we can plot a straight line (red line) having slope equal to the average of slopes for the entire set of data points. The green dots in the graph denote each (height,weight) pair from the data.  
'''
~     

# ocean_45


# ocean_46
def matrixSum(): # creating a function to calculate the sum of the 2 matrices
    # taking 2 square matrices as input from the user 
    print("Enter 2 square matrices of the same order : ")
    a = eval(input())
    b = eval(input())
    n = len(a) # storing the order of the matrix in a variable n
    ans = [[] for i in range(n)] # creating a list 'ans' of the same order to hold the sum of a and b
    for i in range(n): # iterating through each row
        for j in range(n): # iterating through each column
            ans[i].append(a[i][j]+b[i][j]) # appending the value of each element of the sum matrix in ans
    return ans # returning the ans

print(matrixSum())

# ocean_47
def matrixProduct(): # creating a function to calculate the product of 2 given matrices
    # taking 2 square matrices as input from the user
    print("Enter two square matrices : ")
    l1 = eval(input())
    l2 = eval(input())
    n = len(l1) # storing the order of these matrices in a variable 'n'
    product_matrix = [[0 for i in range(n)] for x in range(n)] # intializing a 2D list with all elements as zero to store the product of the matrices

    # using loops to iterate through the elements of matrix represented as 2D lists
    for i in range(n):
        for j in range(n):
            for k in range(n):
                product_matrix[i][j]+=l1[i][k]*l2[k][j] # calculating and updating the value of each element of the product matrix


    return product_matrix # returning the product matrix

print(matrixProduct()) # calling the matrixProduct function

# ocean_48
def writeNaturalNumbers(): # creating a function to write the first n natural numbers to the file output.txt
    n = int(input("Enter the value of n : ")) # taking the value of n from the user
    with open('output.txt','w') as f: # opening the file output.txt through the file handle f
        for i in range(1,n+1): 
            f.write(i+"\n") # writing the first n natural numbers to output.txt
    f.close() # closing the file 

writeNaturalNumbers() # calling the function output.txt 

# ocean_49 
def readWrite(): # creating a function to read a file output.txt and print its contents 
    with open('output.txt','r') as f: # opening the file through file handle f
        line = ' ' # creating an empty string to hold the contents of the file
        while(line): # iterating through each line of the file
            line = f.readline() # reading each line of the file
            print(line) # printing the line read
        f.close() # closing the file after printing its contents 

readWrite() # calling the function readWrite created earlier

# ocean_50
# i have devided the whole pattern in 4 units and have written 4 individual functions to print the completer pattern
def rotate_1(l): # 1st function to print the top left part # it is the reflection of the pattern for the previous case about the line x=y
    for i in l :
        x,y = i
        ans_list_1.append((y,x)) # appending the mirror image of each point about the line x=y from the previous pattern

def shift_1 (l,n): # 2nd function to print the bottorm right part # it just shifts the pattern for the previous case down by 2**(n-1) units
    for i in l :
        x,y = i
        ans_list_1.append((x+(2**(n-1)),y)) # appending the shifted points in the ans_list_1

def shift_2 (l,n): # 3rd function to print the bottom right part of the pattern # it just shifts the pattern for the previous case down and right by 2**(n-1) units
    for i in l :
        x,y = i
        ans_list_1.append((x+(2**(n-1)),y+(2**(n-1)))) # appending the shifted points in the ans_list_1

def rotate_2(l,n): # 4th function to print the top right part of the pattern # it is the mirror image of the points produced by the function rotate_1 about the line y = 2**n
    for i in range(4**(n-1)-1,-1,-1):
        x,y = l[i]
        y = 2**n -(y-1)
        ans_list_1.append((x,y)) # appending the required points in the ans_list_1

def SFC(n): # creating a function SFC to call the above defined 4 functions orderly
    global ans_list_1,l # using global keyword to ensure that the global values of l and ans_list_1 are updated
    j = 1 
    # calling the above defined 4 functions according to the user input
    while j!=n+1:
        rotate_1(l)
        if (j==1):
            j+=1
        if (n==1):
            print(ans_list_1)
            return None
        shift_1(l,j)
        shift_2(l,j)
        rotate_2(ans_list_1,j)
        l = ans_list_1 # updating the value of l for each iterating of the loop
        if(j!=n):
            ans_list_1=[]
        j+=1
    print(ans_list_1) # printing the pattern


l =[(1,1),(2,1),(2,2),(1,2)] # initiating a list l with the first 4 points of the pattern
ans_list_1 = [] # creating an empty list to hold the pattern

print("\n\n # Space Filling Curve # \n")
n = int(input("Enter the number of rows :")) # taking the value of n from user 
print("\n")
SFC(n) #calling the SFC function 

# ocean_51
def bubbleSort(l): # creating a function to sort a list using bubble sort technique
    n = len(l) # storing the length of l in n
    swaps = True # creating a variable swaps which is True or False if number of swaps are greater than 0 or o respectively
    while swaps: # iterating through the list again and again until the number of swaps becomes zero 
        swaps = False # swaps is zero in the begining 
        for i in range(n-1):
            if l[i]>l[i+1]: # swapping l[i] and l[i+1] if they are arranged wrong
                l[i],l[i+1]=l[i+1],l[i]
                swaps = True # assigning True to swaps after any swap
    return(l) # returning the sorted list 

l = eval(input("Enter a list of numbers :")) # taking a list as an input form the user 
print(bubbleSort(l)) # calling the bubbleSort function and printing the sorted list 

# ocean_52
def mergeSort(arr): # creating the function mergeSort to sort a list through merge sort method
    if(len(arr)>1): # base condition - length of list > 1 (because list having single element is already sorted)
        mid = len(arr)//2 # finding the middle index in the list to divide it in 2 halves
        # assigning the two half lists to the variables left and right
        left = arr[0:mid]
        right = arr[mid:]
        # calling mergeSort function on both half lists 
        mergeSort(left)
        mergeSort(right)
        i,j,k = 0,0,0 # intiating i,j,k to hold the index of left , right where comparisons are happening and that of arr where it is being updated 
        # merging two sorted lists left and right
        while(i<len(left) and j<len(right)):
            if(left[i]>right[j]): # compairing the elements of left and right 
                arr[k]=right[j] # updating arr
                j+=1 # incrementing j
            else :
                arr[k]=left[i] # updating arr
                i+=1 # incrementing i
            k+=1 # incrementing k
        # updating remaining part of arr
        while(i<len(left)):
            arr[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            arr[k]=right[j]
            j+=1
            k+=1


l = eval(input('Enter a list of numbers : ')) # taking a list as input from the user 
mergeSort(l) # calling the mergeSort function on l
print(l) # printing l after sorting 

# ocean_53
def quickSort(arr): # defining the function quickSort
    if (len(arr)>1): # checking the base condition 
        pivot = arr[-1] # selecting the last element of the arr as the pivot element 
        left = [i for i in arr[:-1] if i<=pivot] # storing the elements smaller than the pivot element in a list named left
        right = [i for i in arr[:-1] if i>pivot] # storing the elements greater than the pivot element in a list named right
        return quickSort(left) + [pivot] + quickSort(right) # calling the quickSort function recursively to sort the entire list 
    return arr # returning the same list if base condition isn't fulfilled 
    
l = eval(input("Enter a list of numbers : ")) # taking a list of numbers as input from the user 
print(quickSort(l)) # calling the quickSort function on l

# ocean_54
# creating a function BinarySeach to search for an element in a sorted array 
def BinarySearch(arr,key): 
    start = 0 
    end = len(arr)-1
    mid = (start+end)//2
    while(start<=end):
        if arr[mid]==key: # returning the index if key is found 
            return mid
        elif arr[mid]>key: # updating the value of end if arr[mid] is greater than key as this means that key lies on the right of mid
            end = mid-1
        else :
            start = mid+1 # updating the value of start if arr[mid] is smaller than key as this means that key lies on the left of mid
        mid = (start+end)//2
    return -1 # returning -1 if key isn't present in the array

# taking the array and key as input from the user
arr = eval(input('Enter a sorted array :'))
key = int(input('Enter the number you want to search in the array :'))

print(BinarySearch(arr,key)) # calling the BinarySearch function

# ocean_55
# 
import random

def mergeSort(arr): # creating the function mergeSort to sort a list through merge sort method
    if(len(arr)>1): # base condition - length of list > 1 (because list having single element is already sorted)
        mid = len(arr)//2 # finding the middle index in the list to divide it in 2 halves
        # assigning the two half lists to the variables left and right
        left = arr[0:mid]
        right = arr[mid:]
        # calling mergeSort function on both half lists 
        mergeSort(left)
        mergeSort(right)
        i,j,k = 0,0,0 # intiating i,j,k to hold the index of left , right where comparisons are happening and that of arr where it is being updated 
        # merging two sorted lists left and right
        while(i<len(left) and j<len(right)):
            if(left[i]>right[j]): # compairing the elements of left and right 
                arr[k]=right[j] # updating arr
                j+=1 # incrementing j
            else :
                arr[k]=left[i] # updating arr
                i+=1 # incrementing i
            k+=1 # incrementing k
        # updating remaining part of arr
        while(i<len(left)):
            arr[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            arr[k]=right[j]
            j+=1
            k+=1

def quickSort(arr): # defining the function quickSort
    if (len(arr)>1): # checking the base condition 
        pivot = arr[-1] # selecting the last element of the arr as the pivot element 
        left = [i for i in arr[:-1] if i<=pivot] # storing the elements smaller than the pivot element in a list named left
        right = [i for i in arr[:-1] if i>pivot] # storing the elements greater than the pivot element in a list named right
        return quickSort(left) + [pivot] + quickSort(right) # calling the quickSort function recursively to sort the entire list 
    return arr

def bubbleSort(l): # creating a function to sort a list using bubble sort technique
    n = len(l) # storing the length of l in n
    swaps = True # creating a variable swaps which is True or False if number of swaps are greater than 0 or o respectively
    while swaps: # iterating through the list again and again until the number of swaps becomes zero 
        swaps = False # swaps is zero in the begining 
        for i in range(n-1):
            if l[i]>l[i+1]: # swapping l[i] and l[i+1] if they are arranged wrong
                l[i],l[i+1]=l[i+1],l[i]
                swaps = True # assigning True to swaps after any swap
    return(l) # returning the sorted list 

f = open('text.txt')  # opening the file through file handle f
data = f.read() # reading the entire file
arr = data.split() # storing each word of the file in a list arr
x = random.randint(1,3) # generating a random integer between 1-3 and then sorting the list using mergeSort/quickSort/bubbleSort technique
if (x == 1):
    mergeSort(arr)
elif (x == 2):
    arr = quickSort(arr)
else :
    bubbleSort(arr)
f.close() # closing the file

with open('text.txt','w') as f: # opening the file again in write mode to update the file
    # writing the sorted arr into the file
    for i in arr: 
        f.write(i+'\n')
# ocean_55_report 
OCEAN 55 - REPORT 
For this question , I wrote the code to sort a file containg 1 word per line by bubble sort , merge sort and quick sort techniques.

BUBBLE SORT TECHNIQUE compares two adjacent elements of the list and swaps them if they are arranged in the wrong order .
In the worst case i.e. when the list is sorted in reverse order , this method will have to make n*(n-2)/2 
(or (n-1)+(n-2)+...+2+1 = n*(n-1)/2) comparisons where n is the length of the list . 
Therefore the time complexity of bubble sort is O(n^2) .

MERGE SORT TECHNIQUE divides the list in two subarrays (or two halves) recursively till the length of each subarray is 1(which can be done in log(n) steps).
Then the algorithm merges or recombines these subarrays in sorted fashion till the entire sorted array in obtained (in the worst case , this will take n steps)
Therefore the time complexity of merge sort is O(n*log(n)) 

QUICK SORT TECHNIQUE - in this method , an element of the list is chosen as the pivot and then the list is partitioned about the pivot element i.e. all the elments smaller than the pivot element are placed before it (left) and the rest are placed after it (right) such than the list is divided in three parts , left-pivot-right
This can take n steps to complete .
Then the function calls itself recursively for the left and right part each time after partitioning the list until the length of left and right part becomes one (this can be done in log(n) steps).
In the process the elements already get sorted after which they are just recombined to form the complete sorted list.
Therefore the time complexity of quick sort is O(nlog(n)) but in the worst case(when n is very large), it can be O(n^2) because each time when left and right lists are declared , a lot of comparisons are being done.

Thus we can conclude the following points :-
1. bubble sort is always the slowest algorithm among the three .
2. for smaller values of n , quick sort and merge sort almost take the same time to execute.
3. for larger values of n , merge sort is faster than quick sort (which can also be inferred form its time complexity)

Therefore MERGE SORT IS THE FASTEST among these three sorting algorithms.

# ocean_56

# ocean_57
# kadane's algorithm
def maxSumSubarray_kadaneAlgo(l): # creating a functiton to find the maximum sum in an array by kadane's algorithm
    max_sum = 0 # creating a variable to hold the max. sum 
    current_sum = 0 # creating a variable to hold the current sum 
    for x in l: # iterating through the list
        current_sum = max(0, current_sum + x) # updating the current sum 
        max_sum = max(max_sum, current_sum) # updating the max sum 
    return max_sum # returning the max sum in the array

l = eval(input("Enter a list of numbers : ")) # taking list from the user 
print(maxSumSubarray_kadaneAlgo(l)) # printing the max sum

# brute force method
def maxSumSubarray(l): # creating a function maxSubarray to find the max sum , indices and the subarray
    # creating variables to sub-array,max sum and indices 
    max_subarr = [] 
    max_sum = -2147483647
    indices = ()
    i,j = 0,0 # creating variables to hold the starting and ending index of the current substring 
    n = len(l) # creating a variable to hold the length of l
    # iterating through the string and finding the sum for each subarray
    for i in range(n): 
        for j in range(i+1,n):
            # updating the value of max_sum,max_subarr and indices if sum of current subarray is greater than max_sum
            if(sum(l[i:j])>max_sum): 
                max_sum = sum(l[i:j])
                max_subarr = l[i:j]
                indices = (i,j-1)
    
    # printing the output 
    print("required indexes = ",indices)
    print("required sub-array = ",max_subarr)
    print("max. sum = ",max_sum)

l = eval(input("Enter a list of numbers : ")) # taking list from user 
maxSumSubarray(l) # calling the maxSumSubarray function

# ocean_58

# ocean_59
import random # imorting random module 
def caesarCipher(s): # creating a function to encrypt a string using caesar cipher
    k = random.randint(1,26) # giving a random integer value to k
    # creating 2 lists Ualpha and Lalpha to store the upper and lower case alphabets respectively
    Ualpha = [chr(i) for i in range(65,91)]
    Lalpha = [chr(i) for i in range(97,123)]
    s_encrypted = '' # creating a variable s_encrypted to hold the encrypted string
    for i in s: # iterating through the elements of s
        if i.isupper(): # checking if i is uppercase or lowecase or none
            index = Ualpha.index(i) # storing i's index
            s_encrypted+= Ualpha[(index+k)%26] # adding the encrypted letter in place of i to the string s_encrypted
        # repeating same thing for lowercase chr. too
        elif i.islower():
            index = Lalpha.index(i)
            s_encrypted+= Lalpha[(index+k)%26]
        else : # adding i to s_encrypted if i isn't an alphabet
            s_encrypted+=i
    return (s_encrypted) # returning the encryped string 


s = input("Enter a string : ") # taking a string as input from the user 
print(caesarCipher(s)) # printing the encrypted string 






