import math

def keep_only_msb(x: int) -> int:
    if x <= 0:
        return 0  # Handles 0 or negative integers depending on your requirements
    return 1 << (x.bit_length() - 1)
def Charles_BitSet(n1, n2, i):
	L1 = [1, 2, 3, 4]
	c1, c2 = 0, 0
#	print("n1: {} n2: {}".format(n1 % 2 ** n1 , n2 % 2 ** n2))
	if ((n1 & (1 << i))):
		print("c1: {}".format(c1))
#	print(bin(n1 & (1 << i)))
#	print("Result: ")
#	print((n1 & (1 << i)) == (n2 & (1 << i)))
	T1 = L1[n1]
	T2 = L1[n2]
#	print(L1)
	if ((n1 & (1 << i)) == (n2 & (1 << i))):
		L1[n1] = T2
		L1[n2] = T1
		L1 = L1.copy()
		print(L1)

def Charles_Permutations():
	L = [1, 2, 3, 4]
#	R = [1, 2, 3, 4]
#	for n in range(len(L) - 1):
#		Charles_BitSet(len(L), n, L, R)
	n = 2 ** len(L) - 1
	q = 2 ** len(L) - 1
	for c in range(len(L)):
		nt = 1 << (n.bit_length() - 1)
		print(bin(n))
		n >>= 1
		print(bin(q))
		if ((nt & (1 << n.bit_length())) == (q & (1 << n.bit_length()))):
			print("May swap {} with {}".format(n, q))
#		q >>= 1
#		print(bin(n))
#		print(bin(n ^ q))
#		print(bin(~ (n ^ q)))
#		Charles_BitSet(n, q, c)
#	print(bin(q ^ n))
#	print(n)
	return
	
Charles_Permutations()