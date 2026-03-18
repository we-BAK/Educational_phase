n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []
i = 0

for j in range(m):
    while i < n and arr1[i] < arr2[j]:
        i += 1
    result.append(i)

print(*result)