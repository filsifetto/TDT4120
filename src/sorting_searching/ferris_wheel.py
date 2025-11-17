def task():
    n, x = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()

    left = 0
    right = n - 1

    count = 0

    while left <= right:
        if left == right:
            count += 1
            left += 1
        elif P[left] + P[right] <= x:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1
    
    print(count)

task()
