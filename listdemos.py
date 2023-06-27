'''l=list(map(int,input("Enter elements in to the list:").split(" ")))
#for i in l:
    #print("Frequency of",i,"is:",l.count(i))
n=sum(l)/len(l)
print(n)
m=[1,2,3,4,5]
l=l+m
print(l)
'''
l=[2,3,4,5,6]
m=[1,7,8,9,10]
i=0
j=0
n1=len(l)
n2=len(m)
n=[]
while(i<n1 and j<n2):
    if(l[i]<m[j]):
        n.append(l[i])
        i=i+1
    else:
        n.append(m[j])
        j=j+1
while(i<n1):
    n.append(l[i])
    i=i+1
while(j<n2):
    n.append(m[j])
    j=j+1
print(n)
    

    
        