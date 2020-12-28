from collections import Counter
t = int(input())
for i in range(t):
    a = list(input())
    b = list(input())
    x = Counter(a)
    y = Counter(b)
    x.subtract(y)
    print(sum(abs(i) for i in x.values()))