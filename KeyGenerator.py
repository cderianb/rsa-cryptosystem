from operator import mod
import os
import random

from scipy import rand
from sympy import re
import PrimalityTester.FermatLittleTheorem as otd
import lib.ModInverse as mi
from dotenv import load_dotenv

load_dotenv()

INT_LENGTH = int(os.getenv('BIT_LENGTH'))

def is_prime(number:int)->bool:
    return otd.is_prime(number, 1)

def random_prime(bit:int=8)->int:
    prime = 1
    while not is_prime(prime):
        prime = random.getrandbits(bit)
    return prime

def validate_public_key(e:int, T:int) -> bool:
    #Public key must fulfill these following condition
    
    #Must less than T
    if e >= T:
        print(f"{e} >= {T}")
        return False

    #Must not factor of T
    if T % e == 0:
        print(f"{T} % {e} == {T % e}")
        return False
    
    return True

def generate_key_pair(e:int, P:int=1, Q:int=1):
    # The totient always be divisible by 2
    if e == 2:
        return f"public key must greater than 2 and prime"
    #Must Prime
    if not is_prime(e):
        return f"{e} is not a prime number"

    T = 0
    while P==Q or not validate_public_key(e, T):
        P, Q, T = 1, 1, 0
        while P == 0 or not is_prime(P):
            P = random.getrandbits(INT_LENGTH)
        while Q == 0 or not is_prime(Q):
            Q = random.getrandbits(INT_LENGTH)

        N = P*Q
        T = (P-1)*(Q-1)
    d = mi.mod_inverse(e, T)
        
    print("===========RESULT============")
    print(f"P = {P}")
    print(f"Q = {Q}")
    print(f"T = {T}")
    print(f"N = {N}")
    print(f"e = {e}")
    print(f"d = {d}")
    print("=============================")
    
    return (N, e), d

def verify(N, e, d)->bool:
    plain = random.getrandbits(INT_LENGTH)
    print(f"plain = {plain}")

    chiper = (plain**e) % N
    print(f"chiper = {chiper}")

    decrypted = (chiper**d)%N
    print(f"decrypted = {decrypted}")

    if decrypted == plain:
        print("Key Verified")
        return True
    else:
        print("Key invalid")
        return False

print(generate_key_pair(int(input())))