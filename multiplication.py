n=int(input("Enter the number:"))
for i in range(1,11):
    #print(type(i))
    print(n," * ",i," = ",n*i)
#factorial of a number
def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
fact=factorial(n)
print(fact)
