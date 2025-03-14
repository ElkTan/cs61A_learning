def solve(x):
    curr_n=n
    b=t.copy()
    sum=0
    index=x
    num=1
    while True:
        if num >n: 
            break
        if b[index]==num:
            sum+=num 
            b.pop(index)
            curr_n-=1
            if curr_n==0:
                break
            index=index%curr_n
            num=1
        else :
            num+=1
            index+=1
            index=index%curr_n
    return sum

n=int(input())
t=[]
t = list(map(int, input().split())) 
ans=-1
for i in range(n):
    if solve(i)>ans:
        ans=solve(i)
print(ans)

