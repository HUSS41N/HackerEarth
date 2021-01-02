from string import ascii_lowercase,ascii_uppercase
s = input()
k  = int(input())
nums = '0123456789'
ns = ''
for i in s:
    if i.isalpha():
        if i in ascii_uppercase:
            ns += ascii_uppercase[(ascii_uppercase.find(i)+k)%26]
        elif i in ascii_lowercase:
            ns += ascii_lowercase[(ascii_lowercase.find(i)+k)%26]
    elif i.isdigit():
        ns += nums[(nums.find(i)+k)%10]
    else:
        ns += i
print(ns)