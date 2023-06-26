def gcdExtended(a: int, b: int) -> tuple:
	if a == 0:
		return b, 0, 1
	gcd, x1, y1 = gcdExtended(b%a, a)
	x = y1 - (b//a) * x1
	y = x1
	return gcd, x, y
	
def gcdSimple(a: int, b: int) -> int:
	r = a%b
	while r:
		a = b
		b = r
		r = a%b
	last_r = b
	return last_r
