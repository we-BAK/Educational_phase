n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
window_sum = 0
max_length = 0
for right in range(n):
    window_sum += arr[right]
    while window_sum > m:
        window_sum -= arr[left]
        left += 1
    max_length = max(max_length, right - left + 1)
print(max_length)