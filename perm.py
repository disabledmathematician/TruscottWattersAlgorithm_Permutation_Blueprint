def Charles_BitSet(n1, n2, i):
	print(bin(n1 & (1 << i)))
	print("Result: ")
	print((n1 & (1 << i)) == (n2 & (1 << i)))


def Charles_Permutations():
	L = [1, 2, 3, 4]
#	R = [1, 2, 3, 4]
#	for n in range(len(L) - 1):
#		Charles_BitSet(len(L), n, L, R)
	n = len(L)
	q = len(L)
	for c in range(len(L) - 1):
		n >>= 1
		print(bin(n))
		print(bin(n ^ q))
		print(bin(~ (n ^ q)))
		Charles_BitSet(n, q, c)
#	print(bin(q ^ n))
#	print(n)
	return
	
Charles_Permutations()