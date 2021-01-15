import sys
min=-sys.maxsize-1
N,list1=int(input()),[int(x) for x in input().split()]
l1=len(list1)
list2,list2[0],a,b=[0 for i in range(l1+1)],0,1,l1+1
for i in range(a,b): 
    val=min
    for j in range(i): 
        val=max(list2[i-j-1]+list1[j],val) 
    list2[i]=val
print(list2[l1])