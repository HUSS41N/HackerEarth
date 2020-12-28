from string import ascii_lowercase
s = list(input())
sum = 0
lowerCaseLetters = list(ascii_lowercase)
for i in s:
    if i in s:
        sum += lowerCaseLetters.index(i) + 1
print(sum)