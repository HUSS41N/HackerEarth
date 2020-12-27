s = input()
# Brute Force Method first
# def palindrome(s):
#     if s== s[::-1]:
#         return 'YES'
#     else:
#         return 'NO'
# print(palindrome(s))
def palindrome(s):
    left_pointer,right_pointer = 0,len(s)-1
    while left_pointer<right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return 'NO'
        left_pointer +=1
        right_pointer -=1    
    return 'YES'
print(palindrome(s))