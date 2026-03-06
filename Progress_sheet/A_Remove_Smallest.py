t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    j=1
    arr.sort()
    Flag="YES"
    while  j < n:
        if arr[j]-arr[i] >1:
            Flag="NO"
            break
        j+=1
        i+=1
    print(Flag)
    

            
            
        
        
    