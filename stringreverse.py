def reverse(s,s1):
    if len(s)==0:
        return s1
    else:
        s1=s1+s[-1]
        s=s[0:len(s)-1]
        return reverse(s,s1)
s=input("Enter string:")
s1=""
print(reverse(s,s1))

