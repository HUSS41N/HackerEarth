T = int(input())
# middle_seat = [2]
# aside_seat = [3,4]
# window_seat = [1]
# for i in range(1,109):
#     if i % 6 == 0:
#         window_seat.append(i)
#         window_seat.append(i+1)
# i = 2
# while i<108:
#     middle_seat.append(i+3)
#     i += 3
# j = 4
# while j < 108:
#     aside_seat.append(j+5)
#     aside_seat.append(j+6)
#     j += 6
for i in range(T):
    n = int(input())
    n = n + 2 * (6 - (n - 1) % 12) - 1
    if n % 6 < 2:
        print(n, 'WS')
    elif n % 6 == 2 or n % 6 == 5:
        print(n, 'MS')
    else:
        print(n , 'AS')
