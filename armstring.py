s1=input("Enter the number")
l1=[]
l1=list(map(int,s1))
n1=int(s1)
sum=0
for i in range(len(l1)):
    sum=sum+l1[i]**len(s1)
if(sum==n1):
    print("Armstrong")
else:
    print("Not Armstrong")
#fibonacci
def fibonaccise(a,b,n):
    if n==0:
        return 
    else:
        c=a+b
        print(c)
        a=b
        b=c
        fibonaccise(a,b,n-1)
n=int(input("Enter the number:" ))
a=0
b=1
c=0
print(a)
print(b)
print("recursion")
n=n-2
fibonaccise(a,b,n)
print("Non recursion")
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c
#recursion
#prime
    print("Hello World")
n1=int(input("Enter number"))
prime=True
for i in range(2,n1):
    if(n1%1==0):
        prime=False
print(prime)