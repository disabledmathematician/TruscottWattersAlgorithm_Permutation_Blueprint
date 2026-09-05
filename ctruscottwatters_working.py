import time


""" Produces the numbers in factorial sequence.


[[(5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 4), (4, 3), (4, 2), (4, 1), (3, 3), (3, 2), (3, 1), (2, 2), (2, 1), (1, 1)]]

[Program finished]

Authored after 6.001x and 6.002x at MITx for a certificate of Computational Thinking

Authored using PyDroid on a Galaxy Note 10+ Aura Glow, where I do all my very good coding """

"""" Should form a basis for swapped indices, to complete the permutation.

Charles Truscott Watters

1A Ann St, Mullumbimby, 2482 NSW Australia

In due course I should be able to prove the correctness of my algorithm to infinity

"""



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
	combo_all = []
	for L in [[1, 2, 3, 4, 5]]:
		combos = []
		c1 = len(L) - 1
		for e in ctruscottwatters_y1(L):
			print("e: {}".format(e.bit_length()))
			for e2 in ctruscottwatters_y2(L):
				print("e2: {}".format(e2.bit_length()))
				if (e.bit_length(), e2.bit_length()) not in combos and (e2.bit_length(), e.bit_length()) not in combos:
					combos.append((e.bit_length(), e2.bit_length()))
				print("Swapping the elements {} and {} is a start".format(e.bit_length(), e2.bit_length()))
				time.sleep(0.2)
		combo_all.append(combos)
	print(combo_all)
CTruscottPermutations()