t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    elite = arr[-1]
    crowd = arr[0] + arr[1]

    i = 2
    j = n - 2

    possible = False

    while i <= j:
        if elite > crowd:
            possible = True
            break
        crowd += arr[i]
        elite += arr[j]
        i += 1
        j -= 1

    print("YES" if possible else "NO")