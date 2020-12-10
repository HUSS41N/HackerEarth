def solve(arr):
	M = 1000000007
	f = 1
	for i in arr:
		f*=i
	return f % M

if __name__ == '__main__':
	n = int(input())
	arr = list(map(int,input().split()))
	x = solve(arr)
	print(x)