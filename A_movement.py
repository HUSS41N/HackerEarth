n = int(input())
if n % 5 == 0:
    print(int(n/5))
elif n % 5 == 1 or 2 or 3 or 4:
    print(int((n/5)+1))