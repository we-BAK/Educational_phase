n=int(input())
arr=list(map(int,input().split()))
left=0
right=n-1
serja=0
dima=0
turn=0
while left <= right:
    if arr[left] > arr[right]:
        value=arr[left]
        left+=1
    else:
        value=arr[right]
        right-=1
    if turn%2==0:
        serja+=value
    else:
        dima+=value
    turn+=1
print(serja,dima)
        