

import math
import random

def is_prime(p):
# Examine if a given number p is prime
    for i in range(2, int(math.sqrt(p))):

        if p % i == 0:
            return False
    return True


def get_prime(size):
# Find a prime number p
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


def is_generator(g, p):
# Examine if a given number g is a generator of Z^*_p
    for i in range(1, p - 1):
        if (g**i) % p == 1:
            return False
    return True


def get_generator(p):
# Create a generator g of Z^*_p
    for g in range(2, p):
        if is_generator(g, p):
            return g



def generate_secret_key(g, p):
# Input: public parameters: g (generator, base), p (modulus)
# Output: shared secret key using Diffie-Hellman Key Exchange
    # Alice
    a = random.randrange(0, p-1)
    # Alice private key a
    A = (g**a) % p
    # Alice public key A

    # Alice publishes A in the public
    print("Alice public key: A ", A)
    
    # Bob
    b = random.randrange(0, p-1)
    #Bob's private key b
    B = (g**b) % p
    #bob's public key B

    #Bob publishes B in the public
    print("Bob public key: B", B)

    #Compute secret key, they should be the same thing
    sKey = pow(A,b) % p
    sKey2 = pow(B,a) % p
    print("this is the secret key twice:", sKey, sKey2)
    
    
    

    

# test case
# Alice and Bob agree on public parameters g, p
p = get_prime(10000)
g = get_generator(p)
# Print public parameters g, p
print(g, p)
# Create shared secret key using Diffie-Hellman Key Exchange 
generate_secret_key(g, p)
