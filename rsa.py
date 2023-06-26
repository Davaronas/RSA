import sys
from encrypting import start_encrypt
from decrypting import start_decrypt
from miler_rabin import is_prime


def print_help():
	print("\n---RSA---")
	print("The program runs in encoding mode by default")
	print("-h --help for help")
	print("-d --decode for decoding")
	print("-p --print_mode only prints out the result instead of writing it in any files")
	print("-v --verbose prints out the steps")
	print("---------\n\n")
	print("The program needs 3 files in the programs directory:")
	print("---\nprimes - this file must contain the two prime numbers that are going to be used, in the first line separated by a space. First prime must be smaller than the second!")
	print("---\neTarget - this file is what you are going to be encoding, needs to be a number inside. If you have a second line with a single number, that's going to be used as a forced secret exponent.")
	print("---\ndTarget - this file is the decoding target, in -d mode this will be decoded. Needs to contain the number that you want to decode and the secret exponent, separated by a space")
	print("---\n\n")
	print("Additionally, if not in -p mode the program will create files to store the results: eRes for encoding, dRes for decoding")
	sys.exit()


set_to_decode = False
set_to_print = False
set_to_verbose = True
do_miller_rabin = False

def set_to_decode_mode():
	global set_to_decode
	set_to_decode = True
	
def set_to_print_mode():
	global set_to_print
	set_to_print = True
	
def set_to_verbose_mode():
	global set_to_verbose
	set_to_verbose = True


run_args = {"-h": print_help,
			"--help": print_help,
			"-d": set_to_decode_mode,
			"--decode": set_to_decode_mode,
			"-p": set_to_print_mode,
			"--print_mode": set_to_print_mode,
			"-v": set_to_verbose_mode,
			"--verbose": set_to_verbose_mode}


def main():
	for arg in sys.argv:
		if arg in run_args:
			run_args[arg]()
	if do_miller_rabin:
		with open("primes") as f:
			for line in f:
				p, q = line.split()
				is_prime(p,2)
				is_prime(q,2)
				is_prime(p,3)
				is_prime(q,3)
				is_prime(p,5)
				is_prime(q,5)
				is_prime(p,7)
				is_prime(q,7)
	#
	if not set_to_decode:
		print("Running in encoding mode...")
		start_encrypt(set_to_verbose, set_to_print)
	else:
		print("Running in decoding mode...")
		start_decrypt(set_to_verbose, set_to_print)


if __name__ == "__main__":
	main()

	

	

