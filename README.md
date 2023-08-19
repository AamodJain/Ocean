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





