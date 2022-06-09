# https://en.wikipedia.org/wiki/Primality_test

# divide all number from 2 until √n 
# because all unique divisors of n are numbers less than or equal to √n 
# for example n=100   √n = 10
# factors are 2, 4, 5, 10, 20, 25, 50
# and 10 25 50 are repeated numbers from 2 4 5 multiplication
# so we don't need to check after 10 (√n)

def is_prime(n:int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True