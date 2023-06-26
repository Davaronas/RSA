def is_prime(p: int, base: int) -> bool:
    p = int(p)
    base = int(base)
    d = 0
    S = 0
    r = 0
    r_max = 0
    d = p - 1
    while d % 2 == 0:
        d = d / 2
        d = int(d)
        S += 1
    for r in range(0, S):
        if r == 0:
           if (base ** d) % p == 1 or (base ** d) % p == p - 1:
               print(f"\n{p} is probably a prime according to the miller rabin test with base {base}\n")
               return True
        elif base ** (d * (2 ** r)) % p == p - 1:
           print(f"\n{p} is probably a prime according to the miller rabin test with base {base}\n")
           return True
    print(f"\n{p} is not prime according to the miller rabin test\n")
    return False