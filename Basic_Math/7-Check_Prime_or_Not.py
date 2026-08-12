def isPrime(n):
    if n < 2: return False
    m = int(n ** 0.5)
    for i in range(2,m + 1):
        if n % i == 0:
            return False
    return True
print(isPrime(7))        
"""
Input: n = 5
Output: true
Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Input: n = 8
Output: false
Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.
"""