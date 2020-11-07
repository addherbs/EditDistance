def permutList(l):
	if not l:
		return [[]]
	res = []
	for e in l:
		temp = l[:]
		temp.remove(e)
		res.extend([[e] + r for r in permutList(temp)])

	return res

print(permutList([1,1,2]))