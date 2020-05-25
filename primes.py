def sieve_of_eratosthenes(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False

    for x in range(2, n):
        if not primes[x]:
            continue

        mult = 2

        while x * mult < n:
            primes[x * mult] = False
            mult += 1

    return { x for x in range(n) if primes[x] }


def all_odd_to_sqrt(n):
    if n < 2:
        return set()

    if n == 2:
        return { 2 }
    
    primes = [2, 3]

    for candidate in range(5, n, 2):
        isprime = True

        for prime in primes:
            if prime * prime > candidate:
                break

            if candidate % prime == 0:
                isprime = False
                break

        if isprime:
            primes.append(candidate)
            
    return set(primes)


def all_6k_plus_minus_1(n):
    if n < 2:
        return set()

    if n == 2:
        return { 2 }
    
    primes = [2, 3]

    for k in range(6, n, 6):
        lo = k - 1
        hi = k + 1
        loprime = True
        hiprime = True

        for prime in primes:
            if prime * prime > hi:
                break

            if hi % prime == 0:
                hiprime = False
                
            if lo % prime == 0:
                loprime = False

            if not hiprime and not loprime:
                break

        if loprime:
            primes.append(lo)

        if hiprime:
            primes.append(hi)

    return set(primes)


def sieve_of_atkin(n):
    # Based on https://en.wikipedia.org/wiki/Sieve_of_Atkin

    if n < 2:
        return set()

    if n == 2:
        return { 2 }

    if n < 5:
        return { 2, 3 }
        
    primes = { 2, 3, 5 }
    is_prime = [False] * n
    
    for x in range(1, n):
        xpart = 4 * x * x

        if xpart >= n:
            break

        for y in range(1, n, 2):
            num = xpart + y * y

            if num >= n:
                break

            r = num % 60

            if r not in { 1, 13, 17, 29, 37, 41, 49, 53 }:
                continue

            is_prime[num] = not is_prime[num]

    for x in range(1, n, 2):
        xpart = 3 * x * x

        if xpart >= n:
            break

        for y in range(2, n, 2):
            num = xpart + y * y

            if num >= n:
                break

            r = num % 60

            if r not in { 7, 19, 31, 43 }:
                continue

            is_prime[num] = not is_prime[num]

    for x in range(2, n):
        xpart = 3 * x * x

        if 2 * x * x + 2 * x - 1 >= n:
            break

        for y in range(x - 1, 0, -2):
            num = xpart - y * y

            if num >= n:
                break

            r = num % 60

            if r not in { 11, 23, 47, 59 }:
                continue

            is_prime[num] = not is_prime[num]

    for x in range(n):
        if not is_prime[x]:
            continue

        primes.add(x)

        xsq = x * x

        mult = 1

        while mult * xsq < n:
            is_prime[mult * xsq] = False
            mult += 2

    return primes

print(sieve_of_atkin(10**6) - sieve_of_eratosthenes(10**6))