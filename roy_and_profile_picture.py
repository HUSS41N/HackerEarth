l = int(input()) #Square side length FB
n = int(input()) #NUmber of photos
for i in range(n):
    w,h = map(int,input().split())
    if w < l or h < l:
        print('UPLOAD ANOTHER')
    elif w >= l and h >= l:
        if w == h:
            print('ACCEPTED')
        else:
            print('CROP IT')
