n = int(input())
arr = list(map(int,input().split()))
possible_answers  = []
for i in range(len(arr)):
    indexed_list = arr[:i] + arr[i+1:]
    if sum(indexed_list) % 7 == 0:
        possible_answers.append(arr[i])
if len(possible_answers) == 0 :
    print(-1)
else:
    x = min(possible_answers)
    print(arr.index(x))