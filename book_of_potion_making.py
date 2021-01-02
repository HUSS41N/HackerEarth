num = list(map(int,input()))
i = 0
sum = 0
if len(num) != 10:
    print('Illegal ISBN') 
else:
    while i <= 9:
        x = (i+1)*num[i]
        sum += x
        x = 0
        i += 1
    if sum % 11 == 0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')