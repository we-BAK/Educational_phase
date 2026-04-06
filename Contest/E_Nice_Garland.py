n=int(input())
s=input()
pos_con=["RGB","RBG","GRB","GBR","BRG","BGR"]
min_changes=float('inf')
for sp in pos_con:
    changes=0
    nice=""
    for i in range(n):
        L=sp[i%3]
        nice+=L
        if s[i]!=L:
            changes+=1
    if changes< min_changes:
        min_changes=changes
        result=nice
print(min_changes)
print(result)
    
