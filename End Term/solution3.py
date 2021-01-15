import sys 
min=-sys.maxsize-1
list1,m,r=[],100,1000
for x in range(r): 
    val=[] 
    for y in range(m): 
        val1=[] 
        for M in range(m): 
            val1.append(0) 
        val.append(val1) 
    list1.append(val)
def func(num1,num2): 
    s1,s2=0,0
    while(num1): 
        s1=s1+(num1%10)
        num1//=10
    while(num2): 
        s2=s2+(num2%10)
        num2//=10
    res=(s1*s2)
    return res
def ques3(N,M,A,x,n,bef): 
    if(n==M): 
        return 0
    if(x==N): 
        return min
    if(list1[x][n][bef]): 
        return list1[x][n][bef] 
    if(n&1): 
        res2=(func(A[bef],A[x])+ques3(N,M,A,x+1,n+1,x)) 
    else: 
        res2=ques3(N,M,A,x+1,n+1,x) 
    res1=ques3(N,M,A,x+1,n,bef) 
    list1[x][n][bef]=max(res2,res1) 
    return list1[x][n][bef] 
N,A,M=int(input()),list(map(int,input().split())),int(input())
print(ques3(N,M,A,0,0,0))