t = int(input())
for i in range(t):
    n = int(input())
    p = 1
    while n>=1:
        print('*'*p+(n-1)*'#'*2+'*'*p)
        n = n -1
        p += 1