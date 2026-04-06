z=input()
x=input()
vowels="aeiou"
flag=True
if len(z)!=len(x):
    print("No")
else:
    for i in range(len(z)):
        if (z[i] in vowels )!= (x[i] in vowels) :
            flag=False
            break
    if flag:
        print("Yes")
    else:
        print("No")
            
            
    