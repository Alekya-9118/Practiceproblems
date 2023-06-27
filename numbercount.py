'''l=[]
print("Enter elements in to the list:")
l=list(map(int,input().split(" ")))
print(l)
n=input("Enter element to be searched:")
if n in l:
    print(l.index(n))
else:
    print("Not Found")
for i in range(len(l)):
    if(l.count(l[i])==1):
        print(l[i])
       
#swapping
l[0],l[-1]=l[-1],l[0]
print(l)
 '''
#finding element at particular position
#x=int(input("Enter the position:"))
#print(l[x])
m=[2,3,4,5]
n=[6,7,3,2]
for i in m:
    if i in n:
        print(i)

