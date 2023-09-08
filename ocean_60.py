import string

def textstrip(filename):
    with open(filename) as f:
        data = f.read()
        s = ''
        for i in data :
            if i in string.ascii_lowercase:
                s+=i
        return(s)

def letter_distribution(s):
    d = {}
    for i in string.ascii_lowercase:
        d[i]=0
    for i in s:
        d[i] += 1
    return(d)

def substitution_encrypt(s,d):
    ans = ''
    for i in s :
        if i.isalpha():
            ans+= d[i]
        else :
            ans += i
    return ans

def substitution_decrypt(s,d):
    ans = ''
    decrypt = {}
    for i in d:
        decrypt[d[i]] = i
    for i in s:
        if i.isalpha():
            ans+= decrypt[i]
        else :
            ans += i
    return ans

def cryptanalyse_substitution(s):
    freqOrderString = 'etaonrishdlfcmugypwbvkjxzq'
    substitution = {}
    
    letterFreq = {}
    for i in string.ascii_lowercase:
        letterFreq[i]=0
    for i in s:
        letterFreq[i] += 1
    letterFreq_rev = {}
    for i in letterFreq:
        letterFreq_rev[letterFreq[i]] = i
    freq = list(letterFreq_rev.keys())
    freq.sort(reverse=True)
    for i in range(26):
        substitution[freqOrderString[i]]=letterFreq_rev[freq[i]]
    return substitution

def vigenere_encrypt(s,password):
    l = [i for i in string.ascii_lowercase]
    key = str(password)
    n = len(key)
    i = 0
    s_encrypt = ''
    for j in s:
        if (i==n):
            i = 0
        s_encrypt += l[(l.index(j)+int(key[i]))%26]
        i+=1
    return s_encrypt

def vigenere_decrypt(s,password):
    l = [i for i in string.ascii_lowercase]
    key = str(password)
    n = len(key)
    i = 0
    s_encrypt = ''
    for j in s:
        if (i==n):
            i = 0
        s_encrypt += l[(l.index(j)-int(key[i]))%26]
        i+=1
    return s_encrypt


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
        maxi = max(list1)
        newIndex = letters.index(list(letterFreq.keys())[list(letterFreq.values()).index(maxi)])
        print(letters[newIndex])
        password += str(abs(newIndex - 4))
    return password


s = textstrip('text.txt')
# d = {'a':'t','t':'q','q':'w','w':'e','e':'s','s':'f','f':'g','g':'y','y':'u','u':'j','j':'k','k':'n','n':'m','m':'o','o':'p','p':'y','y':'d','d':'i','i':'h','h':'r','r':'z','z':'v','v':'c','c':'b','b':'l','l':'x','x':'a'}
# print(len(d))
#a = substitution_encrypt(s,d)
# print(cryptanalyse_substitution(s))
# print('etaonrishdlfcmugypwbvkjxzq')
#s = 'aamodjainisagoodboyhelikescodingandlisteningmusichedoesentlikecringethinsalsoheusedtolikeplayinchessalotandalsowatchinganimebutwhatcanbedonenowjeeadvancedhasreallytakenatollonhimmaybeandsohasiitrpar'
p = 123
a = (vigenere_encrypt(s,p))
# print(a)
print(cryptanalyse_vigenere_afterlength(a,3))


