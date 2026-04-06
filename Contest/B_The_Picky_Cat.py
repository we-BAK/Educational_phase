t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  target = abs(a[0])

  c = 0
  for i in a:
    if abs(i) <= target:
      c += 1
  if c <= (n//2) + 1:
    print("YES")
  else:
    print("NO")