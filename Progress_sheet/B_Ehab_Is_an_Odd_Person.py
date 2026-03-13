n = int(input())
a = list(map(int, input().split()))

even = False
odd = False

for x in a:
    if x % 2 == 0:
        even = True
    else:
        odd = True

if even and odd:
    a.sort()

print(*a)