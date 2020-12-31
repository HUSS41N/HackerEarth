t = int(input())
for i in range(t):
    sh,sm,eh,em = map(int,input().split())
    s = sh*60 + sm
    m = eh*60 + em
    c = abs(m-s)
    print(c//60,c%60)