n = int(input())
s = input()

def split_houses(s):
    s = s.replace('.','B')
    for i in range(len(s)-1):
        if s[i] == 'H' and s[i+1] == 'H':
            return f'NO\n{s}'
    return f'YES\n{s}'
print(split_houses(s))
