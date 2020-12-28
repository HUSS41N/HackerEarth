vowels = list('aeiou')
count = 0
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    for i in range(n-1):
        if s[i] not in vowels:
            if s[i+1] in vowels:
                count += 1 
    print(count)
    count = 0