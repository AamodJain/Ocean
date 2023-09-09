# importing time module
import string 
import time

# defining textstrip function
def textstrip(filename):
    # opening file through filehandle f
    with open(filename) as f:
        data = f.read() # reading the data present in the file and storing it in a variable named 'data'
        s = '' # creating an empty string to store the required string
        # iterating through the data
        for i in data :
            if i in string.ascii_lowercase:
                # adding the lowercase letters present in the file to s
                s+=i 
        # returning s
        return(s) 

# defining letter_distribution function
def letter_distribution(s):
    # creating an empty dict. to hold the letter distribution 
    d = {}
    # initializing the freq. of each letter as 0
    for i in string.ascii_lowercase:
        d[i]=0
    # iterating through the string s
    for i in s:
        #updating the dictionary 'd'
        d[i] += 1
    # returning d
    return(d)

# defining substitution_encrypt function
def substitution_encrypt(s,d):
    # creating an empty string to hold the encrypted text 
    ans = ''
    # iterating through the string s
    for i in s :
        # checking if i is an alphabet
        if i.isalpha():
            # updating ans
            ans+= d[i]
        else :
            # updating ans with the same element if it is not an alphabet
            ans += i
    # returning ans (encrypted text)
    return ans

# defining substitution_decrypt function
def substitution_decrypt(s,d):
    # creating an empty string to hold the decrypted text 
    ans = ''
    # creating a dict. decrypt to hold the reverse of the substitution used to encrypt the string
    decrypt = {}
    # iterating through d
    for i in d:
        # updating dict. decrypt
        decrypt[d[i]] = i
    # iterating through s
    for i in s:
        if i.isalpha():
            # updating ans with decrypted letters
            ans+= decrypt[i]
        else :
            ans += i
    # returning ans
    return ans

# defining cryptanalyse_substitution function
def cryptanalyse_substitution(s):
    # creating a string freqOrderString to hold the general frequency order of english alphabets
    freqOrderString = 'etaoinfhrdlpcumwfybvkjxqzy'
    # creating an empty dict. to hold the substitution used 
    substitution = {}
    # creating an dict. to hold the letters and their respective frequencies
    letterFreq = letter_distribution(s)
    # creating an empty dict. to hold the reverse key val. pairs of the dict. letterFreq
    letterFreq_rev = {}
    # iterating through letterFreq and updating letterFreq_rev
    for i in letterFreq:
        letterFreq_rev[letterFreq[i]] = i
    # creating a list freq to hold the freq. of the letters
    freq = list(letterFreq_rev.keys())
    # sorting the list freq in descending order 
    freq.sort(reverse=True)
    # updating substitution dict. by comparing freqOrderString and the letterFreq_rev
    for i in range(26):
        substitution[freqOrderString[i]]=letterFreq_rev[freq[i]]
    # returning substitution
    return substitution

# defining vigenere_encrypt function
def vigenere_encrypt(s,password):
    # creating a list to hold all the english alphabets
    l = [i for i in string.ascii_lowercase]
    # storing password as a string in a variable key
    key = str(password)
    # storing the length of pass. in n
    n = len(key)
    i = 0
    # creating an empty string to hold the vignere encrypted string
    s_encrypt = ''
    # iterating through s
    for j in s:
        # checking some conditions and updating s_encrypt accordingly
        if (i==n):
            i = 0
        s_encrypt += l[(l.index(j)+int(key[i]))%26]
        i+=1
    # returning s_encrypt
    return s_encrypt

# defining vigenere_decrypt function
def vigenere_decrypt(s,password):
    # creating a list to hold all the english alphabets
    l = [i for i in string.ascii_lowercase]
    # storing password as a string in a variable key
    key = str(password)
    # storing the length of pass. in n
    n = len(key)
    i = 0
    # creating an empty string to hold the vignere decrypted string
    s_decrypt = ''
    # iterating through s
    for j in s:
        # checking some conditions and updating s_decrypt accordingly
        if (i==n):
            i = 0
        s_decrypt += l[(l.index(j)-int(key[i]))%26]
        i+=1
    # returning s_decrypt
    return s_decrypt


def rotate_compare(s,r):
    s_rotated = s[r:]+s[:r]
    n = len(s)
    collisions = 0
    for i in range(n):
        if s[i]==s_rotated[i]:
            collisions+=1
    return (collisions/n)*100
    
    

def cryptanalyse_vigenere_afterlength(s,k):
    password = ''
    l = ['' for i in range(k)]
    for i in range(k):
            print('hi')
            j = 0
            while (j*(k+i) < len(s)):
                l[i]+=s[j*(k+i)]
                j+=1
    letters = [i for i in string.ascii_lowercase]
    print(l)
    for s in l:
        letterFreq = {}
        for i in string.ascii_lowercase:
            letterFreq[i]=0
        for i in s:
            letterFreq[i] += 1
    
        list1 = list(letterFreq.values())
        list2 = list(letterFreq.keys())
        maxi = 0
        maxi_index = 0
        for i in range(26):
            if list1[i]>maxi:
                maxi = list1[i]
                maxi_index = i
        max_letter = list2[maxi_index]
        newIndex = letters.index(max_letter)
        print(letters[newIndex])
        password += str(abs(newIndex - 4))
    return password

def cryptanalyse_vigenere_findlength(s):
    collFreq = 0
    n = 0
    while(collFreq<=6):
        n+=1
        collFreq = rotate_compare(s,n)
    return n

def cryptanalyse_vigenere(s):
    passLen = cryptanalyse_vigenere_findlength(s)
    password = cryptanalyse_vigenere_afterlength(s,passLen)
    plainText = vigenere_decrypt(s,password)

    print(f'decrypted text : {plainText}\npassword : {password}')

#s = textstrip('text.txt')
#d = {'a':'t','t':'q','q':'w','w':'e','e':'s','s':'f','f':'g','g':'y','y':'u','u':'j','j':'k','k':'n','n':'m','m':'o','o':'p','p':'y','y':'d','d':'i','i':'h','h':'r','r':'z','z':'v','v':'c','c':'b','b':'l','l':'x','x':'a'}
# print(len(d))
#a = substitution_encrypt(s,d)
# print(cryptanalyse_substitution(s))
# print('etaonrishdlfcmugypwbvkjxzq')
s = 'aamodjainisagoodboyhelikescodingandlisteningmusichedoesentlikecringethinsalsoheusedtolikeplayinchessalotandalsowatchinganimebutwhatcanbedonenowjeeadvancedhasreallytakenatollonhimmaybeandsohasiitrpar'
p = 69
a = (vigenere_encrypt(s,p))
# print(a)
#print(rotate_compare(s,5))
print(a)
start = time.time()
print(vigenere_decrypt(a,p))
End = time.time()
print('time taken :', End-start)

#etaonrishdlfcmugypwbvkjxzq
#etaoinsrhdlucmfywgpbvkxqjz
#etaoinfhrdlpcumwfybvkjxqzy
#print(len(s))




