t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()
    count=0
    i=0
    while i < n-1:
        if s[i] == 'A' and s[i +1] =='B':
            count +=1
            i +=2
        else:
            i +=1
    print(count)
  