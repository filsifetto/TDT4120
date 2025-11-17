def task():
    m, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    a_pointer = 0
    b_pointer = 0
    count = 0

    while a_pointer < len(A) and b_pointer < len(B):
        a = A[a_pointer]
        b = B[b_pointer]

        if abs(a - b) <= k:
            count += 1
            a_pointer += 1
            b_pointer += 1

        elif a < b:
            a_pointer += 1
        else:
            b_pointer += 1

    print(count)

task()
