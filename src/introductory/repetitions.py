A = input()
 
 
 
def find_max(dna):
    max_seq = 0
    i, j = 0, 0
 
    while j < len(A):
        while A[i] == A[j]:
            j += 1
            if j >= len(A):
                return max(max_seq, j - i)
        max_seq = max(max_seq, j - i)
        i = j
 
print(find_max(A))

