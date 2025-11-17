n = int(input())
 
from math import comb
 
for i in range(1, n + 1):
    x = comb(i**2, 2) - 4*(i - 1)*(i - 2)
    print(x)

