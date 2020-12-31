t = int(input())
for i in range(t):
    s1,s2 = input().split()
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    if s1 == s2:
        print('YES')
    else:
        print('NO')