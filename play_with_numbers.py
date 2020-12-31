# import math,statistics

# n,q = map(int,input().split())
# arr = list(map(int,input().split()))

# for i in range(q):
#     left,right = map(int,input().split())
#     print(math.floor(statistics.mean(arr[arr.index(left):arr.index(right)+1])))
from sys import stdin
N, Q = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
B = [0]

for elements in A:
    B.append(elements+B[-1])

 

for _ in range(Q):
    L, R = map(int, stdin.readline().split())
    print((B[R]-B[L-1])//(R-L+1))