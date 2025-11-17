n = int(input())
A = list(map(int, input().split()))
 
def count_moves(A, n):
    roof = A[0]
    count = 0
 
    for i in range(n):
        if A[i] > roof: roof = A[i]
        else:
            count += roof - A[i]
    return count
 
print(count_moves(A, n))

