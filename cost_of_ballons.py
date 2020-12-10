for _ in range(int(input())):

	g,p = map(int, input().split())

	cost1, cost2 = (0,0)

	for i in range(int(input())):

		m,n = map(int, input().split())

		if(m == 1 and n ==1):

			cost1 += (g+p)

			cost2 += (g+p)

		elif m ==1 and n == 0:

			cost1 += g #cost 1 : 1st green and 2nd purple

			cost2 += p #cost 2 : 1st purple and 2nd green

		elif m == 0 and n == 1:

			cost1 += p #cost 1 : 1st green and 2nd purple
			cost2 += g

	print(min(cost1, cost2))