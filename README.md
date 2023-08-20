# Ocean
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

# ocean_37 

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
    global oc
    print(order[oc]*n,end="") # printing the pattern , one unit at a time # considering continuous string of a single letter a one unit
    oc+=1 # incrementing oc after printing one unit of the pattern
    print(order[oc]*n,end="")
    oc+=1 
oc = 0 # creating a variable oc to hold the current index(where printing occurs) in the string order
order = "RULD" # defining the order as Right->Up->Left->Down
i =1 # creating a variable i, to hold the number of times a letter has to be printed
termCount=0 # creating a variable to count the number of terms printed
while(termCount<=1000000):
    if(oc==4):
        oc=0
    miniSpiral(i) # calling the miniSpiral function
    termCount+=2*i # incrementing termCount
    i+=1 # incrementing i

# ocean_41

