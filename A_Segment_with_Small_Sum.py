n, m = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
j = 0
Sum = 0
max_len = 0
while j < n:
    Sum += arr[j]
    while Sum > m:
        Sum -= arr[i]
        i += 1
    max_len = max(max_len, j - i + 1)
    j += 1
print(max_len)