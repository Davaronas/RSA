import traceback
import gcdExt as gcd
import sys

def start_encrypt(set_to_verbose: bool, set_to_print: bool):
	p = q = n = phi_n = m = encoded_message = 0
	forced_e = False
	try:
		with open("primes") as primes:
			with open("eTarget") as r:
				with open("eRes", "w") as w:
					for line in primes:
						p, q = line.split()
					if set_to_verbose:
						print("p: ", p)
						print("q: ", q)
					p = int(p)
					q = int(q)
					n = p * q
					phi_n = (p - 1) * (q - 1)
					if set_to_verbose:
							print("n: ", n)
							print("phi(n): ", phi_n)
							print("\nLooking for e...\n")
					for i, line in enumerate(r):
						if(i == 0):
							m = int(line)
						else:
							e = line
							e = int(e)
							if set_to_verbose:
								print("e was predefined in eTarget: ", e)
							forced_e = True
					if not forced_e:
						e = 2
						_gcd = gcd.gcdSimple(phi_n, e)
						while _gcd != 1:
							if set_to_verbose:
								print(f"({phi_n}, {e}) is bad, gcd is {_gcd}")
							e += 1
							_gcd = gcd.gcdSimple(phi_n, e)
					#
					_gcd, x, d = gcd.gcdExtended(phi_n, e)
					if d < 0:
						d = phi_n + d
					d_check = (e * d) % phi_n
					if(d_check != 1):
						print("e * d is not congruent to one mod phi(n), e was probably predefinied, and is wrong. Quitting...")
						sys.exit()
					if set_to_verbose:
						print("\ne: ", e)
						print("Calculating the Extended Euclidean algorithm to phi(n) and e, to find d")
						print("d: ", d)
						print(f"{e} * {d} is congruent to {d_check} mod {phi_n}")
						print(f"\nPublic key is: ({e}, {n})")
						print(f"Private key is: ({d}, {n})")
					#
					#
					encoded_message = (m ** e) % n
					if not set_to_print:
						w.write(f"Primes: {p} {q}\n")
						w.write(f"Original message: {m}\n")
						w.write(f"Encoded message: {encoded_message}\n")
						w.write(f"Public Key: ({e}, {n})\n")
						w.write(f"Private Key: ({d}, {n})")
						print("\nNot in print mode, writing encoded message to eRes file")
					if set_to_verbose:
						print("\nThe message to encode: ", m)
						print("The encoding will do the following: \nm ^ e mod n")
						print(f"{m} ^ {e} mod {n}")
						print("\nThe encoded message is: ", encoded_message)	
	except Exception as err:
		print(f"Something went wrong, run with -h to see how to use the program\n{err}")
		print(traceback.format_exc())
		
		
		
