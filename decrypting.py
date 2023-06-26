import traceback
import gcdExt as gcd

def start_decrypt(set_to_verbose: bool, set_to_print: bool):
	p = q = c = d = M1 = M2 = M = c1 = c2 = decoded_message = 0
	try:
		with open("primes") as primes:
			with open("dTarget") as r:
				with open("dRes", "w") as w:
					for line in primes:
						p, q = line.split()
					p = int(p)
					q = int(q)
					if set_to_verbose:
						print("p: ", p)
						print("q: ", q)
					for line2 in r:
						c, d = line2.split()
					c = int(c)
					d = int(d)
					c1 = (c ** (d % (p - 1))) % p
					c2 = (c ** (d % (q - 1))) % q
					M1 = q
					M2 = p
					M = M1 * M2
					sq1 = d % (p - 1)
					sq2 = d % (q - 1)
					_gcd, x, y = gcd.gcdExtended(M1,M2)
					decoded_message = ((c1 * x * M1) + (c2 * y * M2)) % M
					#
					if set_to_verbose:
						print("c: ", c)
						print("d: ", d)
						print("\nCalculating the following:")
						print("c1 = c ^ (d mod (p - 1)) mod p")
						print("c2 = c ^ (d mod (q - 1)) mod q")
						print(f"\nc1 = {c} ^ ({d} mod ({p} - 1)) mod {p}")
						print(f"c2 = {c} ^ ({d} mod ({q} - 1)) mod {q}")
						print(f"\nc1 = {c} ^ {sq1} mod {p}")
						print(f"c2 = {c} ^ {sq2} mod {q}")
						print("\nc1: ", c1)
						print("c2: ", c2)
						print("M1: ", M1)
						print("M2: ", M2)
						print("M: ", M)
						print("\nNow we need to get x and y from the Extended Euclidean algorithm, using M1 and M2")
						print("x: ", x)
						print("y: ", y)
						print("\nFinally, we need to calculate the following: \n(c1 * x * M1) + (c2 * y * M2) mod M")
						print(f"({c1} * {x} * {M1}) + ({c2} * {y} * {M2}) mod {M}")
						print("\nThe decoded message is: ", decoded_message)
					if not set_to_print:
						w.write(f"Primes: {p} {q}\n")
						w.write(f"Message to decode: {c}\n")
						w.write(f"Decoded message: {decoded_message}\n")
						w.write(f"Private Key: ({d}, {M})")
						print("\nNot in print mode, writing decoded message to dRes file")
					
				
				
	except Exception as err:
		print(f"Something went wrong, run with -h to see how to use the program\n{err}")
		print(traceback.format_exc())
