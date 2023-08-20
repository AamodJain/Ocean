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





