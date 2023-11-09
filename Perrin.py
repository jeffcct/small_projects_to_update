import math
def extend_primes(primes, max):
    for i in range(primes[-1], max + 1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

def is_prime(num, primes = [2, 3]):
    root = math.floor(math.sqrt(num))
    extend_primes(primes, root)
    for prime in primes:
        if prime > root:
            return True
        if num % prime == 0:
            return False
    return True
        

def main():
    first = 3
    second = 0
    third = 2
    print("3, 0, 2")
    for i in range(3, 100000000):
        next = first + second
        first = second
        second = third
        third = next
        
        isp = is_prime(i)
        mod = next % i
        #print(i, next)
        if mod == 0:
            if not isp:
                print(i, "failed nprime")
        else:
            if isp:
                print(i, "failed prime")
        
main()