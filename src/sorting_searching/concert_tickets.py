import bisect
def task():
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    

    T = list(map(int, input().split()))
    print(T)
    print(prices)

    for t in T:
        index = bisect.bisect_right(prices, t)
        print(t, index)
        if index == -1:
            print(-1)
        else:
            print(prices[index])
            prices = prices[:index] + prices[index + 1:]

task()
