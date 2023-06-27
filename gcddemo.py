'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
while b!=0:
    a,b=b,a%b
print(a)
'''
#finding max element in the list
l=list(map(int,input("Enter elements in to the list:").split(" ")))
max=l[0]
for i in range(1,len(l)):
    if max<l[i]:
        max=l[i]
print(max)
#sum of elements in the list
def sumrec(sum,l,i):
    if(i==len(l)):
        return sum
    else:
        sum=sum+l[i]
        i=i+1
        return sumrec(sum,l,i)
print("recursion")
sum=sumrec(0,l,0)
print(sum)
sum=0
for i in range(len(l)):
    sum=sum+l[i]
print(sum)