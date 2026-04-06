t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s=s.lower()
    z=[]
    if n>0:
        z.append(s[0])
        for i in range(1,n):
            if s[i]!=s[i-1]:
                z.append(s[i])
    z="".join(z)
    if z=="meow":
        print("YES")
    else:
        print("NO")
        
    