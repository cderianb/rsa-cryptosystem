# https://en.wikipedia.org/wiki/Primality_test

# Improvement for TrialDivision algorithm
# all the prime numbers greater than 3 are in the form of 6k ± 1
# all integers are in the form of 6k ± i where i = -1, 0, 2, 3, 4
# 2 divides (6k + 0), (6k + 2), and (6k + 4)
# 3 divides (6k + 3)
# that leaves us 6k ± 1
# thus check through all number in the form of 6k ± 1 < √n

def is_prime(n:int) -> bool:
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False

    # start from 5
    # because because k=1 and 6x1-1 = 5 (6k-1)
    for i in range(5, n, 6):
        if i**2 > n:
            break
        
        if n%i == 0 or n%(i + 2)==0: # plus 2 because 5+2 == 6x1+1
            return False
    return True