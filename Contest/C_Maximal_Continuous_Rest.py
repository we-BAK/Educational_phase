n=int(input())
arr=list(map(int,input().split()))
Max=0
counter=0
arr+=arr
for i in range(n+n):
    if arr[i]==1:
        counter+=1
        Max=max(Max,counter)
    else:
        counter=0
print(Max)