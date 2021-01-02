n = int(input())
arr = list(map(str,input().split()))
num = ''
for i in arr:
    num += i[-1]
if int(num)% 10 == 0:
    print('Yes')
else:
    print('No')