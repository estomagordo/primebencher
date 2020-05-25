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
        return []

    if n == 2:
        return [2]
    
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
        return []

    if n == 2:
        return [2]
    
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