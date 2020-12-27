zoo = input()
z = 0
o = 0
for i in zoo:
    if i == 'z':
        z +=1
    elif i == 'o':
        o += 1

if 2 * z == o:
    print('Yes')
else:
    print('No')