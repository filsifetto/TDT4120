import bisect
def task():
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    

    T = list(map(int, input().split()))

    for t in T:
        index = bisect.bisect_right(prices, t) - 1
        if index == -1:
            print(-1)
        else:
            print(prices.pop(index))

task()
