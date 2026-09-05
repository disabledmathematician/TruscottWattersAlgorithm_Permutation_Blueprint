
def ctruscottwatters_y1(L):
	n = 2 ** len(L) - 1
	q = 2 ** len(L) - 1
	for c in range(len(L)):
		nt = 1 << (n.bit_length() - 1)
		yield nt
		n >>= 1
def ctruscottwatters_y2(L):
	n = 2 ** len(L) - 1
	q = 2 ** len(L) - 1
	for c in range(len(L)):
		nt = 1 << (n.bit_length() - 1)
		yield nt
#		b = (~ nt + 1)
#		print("b: {}".format(b))
#		q = 1 << (q.bit_length() - 1)
#		if ((nt & (1 << n.bit_length() - 1)) == (q & (1 << q.bit_length() - 1))):
#			print("May swap {} with {}".format(nt, q))
		n >>= 1
		

def CTruscottPermutations():
	combos = []
	L = [1, 2, 3]
	c1 = len(L) - 1
	for e in ctruscottwatters_y1(L):
		print("e: {}".format(e.bit_length()))
		for e2 in ctruscottwatters_y2(L):
			print("e2: {}".format(e2.bit_length()))
			if (e.bit_length(), e2.bit_length()) not in combos and (e2.bit_length(), e.bit_length()) not in combos:
				combos.append((e.bit_length(), e2.bit_length()))
			print("Swapping the elements {} and {} is a start".format(e.bit_length(), e2.bit_length()))
	print(combos)
CTruscottPermutations()