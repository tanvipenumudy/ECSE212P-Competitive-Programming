N,list1,list2,X=int(input()),[int(x) for x in input().split()],[int(x) for x in input().split()],int(input())
c,l1,l2=0,len(list1),len(list2)
for i in range(l1):
    for j in range(l2):
        if(X<abs(list2[j]-list1[i])):
            c=c+1
            break
print(c)