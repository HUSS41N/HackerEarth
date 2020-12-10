# You are given an array  of size  that contains integers. Here,  is an even number. You are required to perform the following operations:

# Divide the array of numbers in two equal halves
# Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
# Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
# Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
# Generate a number by using the digits that have been selected in the above steps
# Your task is to determine whether the newly-generated number is divisible by .

# Input format

# First line: A single integer  denoting the size of array 
# Second line:  space-separated integers denoting the elements of array 
# Output format
# If the newly-generated number is divisible by , then print . Otherwise, print .
def solve (A):
    l = int(len(A)/2)
    first_half = A[:l]
    second_half = A[l:]
    num = ''
    for i in first_half:
        i = str(i)
        num += ''.join(i[0][0])
    for i in second_half:
        i = str(i)
        num += ''.join(i[-1][-1])
    if int(num) % 11 == 0:
        print('OUI')
    else:
        print('NON')
if __name__ == '__main__':

	N = int(input())
	A = list(map(int, input().split()))

	solve(A)
