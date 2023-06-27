def palindrome(n,temp):
    if n==0:
        return temp
    temp=temp*10+n%10
    return palindrome(n//10,temp)
#n=int(input("Enter the number:"))
#temp=palindrome(n,0)
#if(temp==n):
    #print("yes")
#else:
    #print("No")
def firstUpper(s):
    if len(s)==0:
        return
    else:
        if(s[0].isupper()):
            return s[0]
        else:
            s=s[1:]
            return firstUpper(s)
s1=input("Enter the string:")
print(firstUpper(s1))
for i in range(len(s1)):
    if(s1[i].isupper()):
        print(s1[i])
        break
#recurion
