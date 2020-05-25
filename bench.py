from time import time
from primes import *


def bench(function, name, exp, repeats=3):
    print(f'Running {name} on 10^{exp} elements, {repeats} times.')
    now = time()

    for x in range(1, repeats + 1):
        res = function(10**exp)
        taken = time() - now
        now = time()

        print(f'Run number {x}: {round(taken, 4)}s')
        print()


def main():
    bench(sieve_of_eratosthenes, 'Sieve of Eratosthenes', 6)
    bench(sieve_of_eratosthenes, 'Sieve of Eratosthenes', 7)
    bench(sieve_of_atkin, 'Sieve of Atkin', 6)
    bench(sieve_of_atkin, 'Sieve of Atkin', 7)
    bench(all_odd_to_sqrt, 'All odd up to square root', 6)
    bench(all_odd_to_sqrt, 'All odd up to square root', 7)
    bench(all_6k_plus_minus_1, 'All 6k +-1 up to square root', 6)
    bench(all_6k_plus_minus_1, 'All 6k +-1 up to square root', 7)

if __name__ == '__main__':
    main()