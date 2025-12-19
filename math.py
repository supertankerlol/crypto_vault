import secrets

def is_prime(n, k=5): # Miller-Rabin primality test
    if n <= 3: return n > 1
    if n % 2 == 0: return False
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = secrets.randbelow(n - 4) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generate_prime(bits=1024):
    while True:
        p = secrets.randbits(bits)
        if p % 2 != 0 and is_prime(p):
            return p

def gcd_extended(a, b):
    if a == 0: return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = gcd_extended(e, phi)
    if gcd != 1: raise Exception('Modular inverse does not exist')
    return x % phi